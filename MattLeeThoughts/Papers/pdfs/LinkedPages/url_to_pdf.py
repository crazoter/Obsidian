#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pdf_downloader.py: Read urls and download them as PDF.
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.1"

from pyhtml2pdf import converter
from multiprocessing import Pool
import os
import re
import urllib.request as request

print_multiproc_pool = 5
scriptdir = os.path.dirname(os.path.abspath(__file__))

def convert_if_arxiv(url):
    url = url.strip()
    if "arxiv.org/abs/" in url:
        result = f"https://arxiv.org/pdf/{url.split('/')[-1]}.pdf"
        print("Converted " + result)
        return result
    return url

def print_pdf(url):
    if url[0] == "#":
        return
    if len(url) <= 0:
        return

    url = convert_if_arxiv(url)
    link_export_folder = scriptdir
    filename = f"{link_export_folder}/{re.sub('[^A-Za-z0-9]+|https?', '', url.replace('.pdf',''))}"
    filename += ".pdf"
    print(f"Generating {filename} from {url}")

    
    if url.endswith(".pdf"):
        try:
            request.urlretrieve(url, filename)
        except Exception as e:
            print(e, url, filename)
        return
    
    converter.convert(url, filename)
    return

if __name__ == "__main__":
    url_file = os.path.join(scriptdir, "./links_to_download.md")
    with open(url_file) as file:
        lines = file.readlines()
        if len(lines) > 0:
            with Pool(print_multiproc_pool) as p:
                print(p.map(print_pdf, lines))
        print("Task complete!")