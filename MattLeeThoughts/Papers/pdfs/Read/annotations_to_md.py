#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
annotations_to_md.py: Extract highlighted text and annotated comments as Markdown using the PyMuPDF library.

Commands:   You can execute commands by typing them into a comment. The comment won't be rendered as markdown.

List of commands:
            !img:           Generate a code snippet for the Better PDF Plugin, which you can use to include a cropped portion of the PDF to act as an image.
            !url={url}:     Specify the url of the PDF. Markdown will be generated to make links to this URL using text fragments.
                            For more info on text fragments, see https://stackoverflow.com/questions/62161819/what-exactly-is-the-text-location-hash-in-an-url
            !urlonly:       Don't archive the PDF.

Possible bugs:
            1. Currently links are attached on a page by page basis, text - text comparison (I don't care if you actually highlighted the link).
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__credits__ = ["edxu96","vinaykhatri","gangula"]
__license__ = "GPL 3.0"
__version__ = "1.0.1"

# https://stackoverflow.com/questions/50801270/extract-comments-from-pdf
import argparse
import fitz
from pyhtml2pdf import converter
from multiprocessing import Pool
import os
from shutil import copyfile
import urllib.parse

# From https://github.com/pymupdf/PyMuPDF/issues/318#issuecomment-658781494
_threshold_intersection = 0.9  # if the intersection is large enough.
link_search_padding = 2
print_multiproc_pool = 5

def _check_contain(r_word, points):
    """If `r_word` is contained in the rectangular area.

    The area of the intersection should be large enough compared to the
    area of the given word.

    Args:
        r_word (fitz.Rect): rectangular area of a single word.
        points (list): list of points in the rectangular area of the
            given part of a highlight.

    Returns:
        bool: whether `r_word` is contained in the rectangular area.
    """
    # `r` is mutable, so everytime a new `r` should be initiated.
    r = fitz.Quad(points).rect
    r.intersect(r_word)

    if r.getArea() >= r_word.getArea() * _threshold_intersection:
        contain = True
    else:
        contain = False
    return contain


def _extract_annot(annot, words_on_page):
    """Extract words in a given highlight.

    Args:
        annot (fitz.Annot): [description]
        words_on_page (list): [description]

    Returns:
        str: words in the entire highlight.
    """
    quad_points = annot.vertices
    quad_count = int(len(quad_points) / 4)
    sentences = ['' for i in range(quad_count)]
    for i in range(quad_count):
        points = quad_points[i * 4: i * 4 + 4]
        words = [
            w for w in words_on_page if
            _check_contain(fitz.Rect(w[:4]), points)
        ]
        sentences[i] = ' '.join(w[4] for w in words)
    sentence = ' '.join(sentences)

    return sentence

def convert_if_arxiv(url):
    if "arxiv.org" in url:
        return f"https://arxiv.org/pdf/{url.split('/')[-1]}.pdf"
    return url

# Helper class for specifying markdown
class MarkdownPiece:
    def __init__(self, text, page_map_links=None, page_no=None, newlines=0, is_quote=False, add_link=False):
        self.is_quote = is_quote
        self.add_link = add_link
        self.original_text = text
        self.page_no = page_no
        self.newlines = '\n' * newlines
        # Generate linked text
        self.linked_text = text
        self.links = {}
        if page_map_links:
            keys_to_delete = []
            for k in page_map_links.keys():
                if k in self.linked_text:
                    self.linked_text = self.linked_text.replace(k, f'[{k}]({page_map_links[k]})', 1)
                    keys_to_delete.append(k)
            # I don't want to replace more than once and clutter the notes with links
            for k in keys_to_delete:
                self.links[k] = page_map_links[k]
                del page_map_links[k]

    def get_text(self, url):
        result = ""
        if self.is_quote:
            result += "> "
        if self.original_text:
            result += self.linked_text
        if self.page_no:
            result += " (p. {0}) ".format(self.page_no)
        if self.add_link and url:
            result += " [\[Context\]]({0}#:~:text={1}) ".format(url, self.original_text)
        if self.newlines:
            result += self.newlines
        return result

def print_pdf(pair):
    # exploratory_filename = urllib.parse.quote_plus(f'{k}'.replace(" ","")) + ".pdf"
    print(f"Generating exploratory PDF @ {pair[1]}")
    converter.convert(pair[0], pair[1])
    return None

def extract_to_md(filepath, outfilepath, filename, link_export_folder):
    """
    filepath: full filepath of the file to read annotations from
    outfilepath: path to output the generated markdown
    filename: name of file (which will be used for images and title)
    """
    with open(outfilepath, "w", encoding="utf-8") as outfile:
        
        archive_file = True
        output_text = []
        page_url = None
        
        # iterate doc
        doc = fitz.open(filepath)
        for page_num in range(doc.pageCount):
            page = doc[page_num]
            visual_page_num = page_num + 1

            # Build links dictionary
            # https://www.techgeekbuzz.com/how-to-extract-all-pdf-links-in-python/
            # https://stackoverflow.com/questions/60655909/extracting-complete-hyperlink-string-from-pdf-using-pymupdf
            # A deque could be faster in practice, but it's not an out-of-the-box solution to pop it in O(1) during iteration
            map_links = {}
            for link in page.links():
                #if the link is an extrenal link with http or https (URI)
                if "uri" in link:
                    url = link["uri"]
                    x = link_search_padding # expand rect to adding padding - change value accordingly
                    link_txt = page.get_textbox(link["from"] + (-x, -x, x, x))
                    if len(link_txt) > 0:
                        # print(f'Text: "{link_txt}" Link: "{url}" found on page number --> {visual_page_num}')
                        map_links[link_txt] = url

            # Iterate through annotations
            pageHasAnnots = False
            words_on_page = None
            for annot in page.annots():
                # Add a page header
                if not pageHasAnnots:
                    pageHasAnnots = True
                    words_on_page = page.getText("words")  # list of words on page
                    output_text.append(MarkdownPiece(f"#### Page {visual_page_num}", newlines=2))

                # Extract the texts
                comments = annot.info["content"]
                highlighted_text = _extract_annot(annot, words_on_page)
                if (len(highlighted_text) > 0):
                    output_text.append(MarkdownPiece(highlighted_text, map_links, visual_page_num, newlines=2, is_quote=True, add_link=True))
                if (len(comments) > 0):
                    if "!urlonly" in comments:
                        archive_file = False
                    elif "!url=" in comments:
                        page_url = comments.split('=')[1]
                        print(f"Extracted url {page_url}\n")
                    elif "!img" in comments:
                        output_text.append(MarkdownPiece((
                            '```pdf\n{{"url": "/Papers/pdfs/Archived/{0}", "page": {1},\n"rect": [0,0,0,0]\n}}\n```\n\n'
                            ).format(filename, visual_page_num))
                        )
                    else:
                        output_text.append(MarkdownPiece(comments, map_links, visual_page_num, newlines=2, is_quote=False, add_link=False))

            # Output line break
            if pageHasAnnots:
                output_text.append(MarkdownPiece('---', newlines=1))

        # If needed, output PDF at the start of the generated markdown
        # if archive_file:
            # output_text.insert(0, MarkdownPiece(f"![[{filename}]]\n\n---\n\n"))

        # Encode as UTF-8 and output to file as UTF-8
        map_links = {}  
        for md in output_text:
            # https://stackoverflow.com/questions/5224089/safe-decoding-in-python-symbol-instead-of-exception
            text = md.get_text(page_url).encode().decode("utf-8", "replace")
            outfile.write(text)

            # Collate links from the markdown
            if md.links:
                for k in md.links.keys():
                    if md.links[k] not in map_links:
                        map_links[md.links[k]] = link_export_folder + '/' + re.sub('[^A-Za-z0-9]+|https?', '', k) + ".pdf"

        # Convert map to list for multiprocessing pool
        links_to_explore = []
        for url in map_links:
            links_to_explore.append((url, convert_if_arxiv(map_links[url])))

        # Actually print the pdfs
        # Might be a good idea to pool everything at the end? but a global variable would be useful. I'm too lazy to design something complicated
        with Pool(print_multiproc_pool) as p:
            print(p.map(print_pdf, links_to_explore))

        return archive_file

    # This should never be reached
    return True

if __name__ == "__main__":
    # Iterate through files in directory
    scriptdir = os.path.dirname(os.path.abspath(__file__))
    archive_folder = os.path.join(scriptdir, "../Archived")
    output_folder = os.path.join(scriptdir, "../Annotations")
    link_export_folder = os.path.join(scriptdir, "../LinkedPages")

    for folder, subfolders, filenames in os.walk(scriptdir):
        for filename in filenames:
            if filename.lower().endswith(("pdf")):
                filepath = os.path.join(folder, filename)
                archive_filepath = os.path.join(archive_folder, filename)
                output_filename = os.path.splitext(filename)[0]+'.md'
                output_filepath = os.path.join(output_folder, output_filename)
                archive_file = extract_to_md(filepath, output_filepath, filename, link_export_folder)
                if archive_file:
                    copyfile(filepath, archive_filepath)
                print("Extracted {0} to {1}\n".format(filename, output_filepath))

    print("Task complete!")