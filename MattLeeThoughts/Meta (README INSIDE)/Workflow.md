#meta
Descript
 ===
 
- The purpose of using a note-taking device is to consolidate information in 1 place (for easy access / revision). 
- Methodology depends on the individual. For me, I think there are 2 key ways of capturing / distilling information:

1. By text:
	1. Summaries written by the user
	2. Text that is copied from the source
	3. Text in an image
2. By images:
	1. Images drawn by the user
	2. Images copied from the source

With additional requirements:
1. Will context / origin of the information be useful? If so, will it be useful to use highlighting on such texts?

#### PC
1. By text:
	1. Summaries written by the user
		1. VERY EASY: By typing
	2. Text that is copied from the source 
		1. VERY EASY: By typing
	3. Text in an image 
		1. EASY: convert using OCR
2. By images:
	1. Images drawn by the user
		1. TROUBLESOME: Can be done using draw.io OR drawing tablet
	2. Images copied from the source
		1. VERY EASY: Crop and paste

#### Tablet
1. By text:
	1. Summaries written by the user
		1. TROUBLESOME: Typing on a tablet is not fast and full of typos
	2. Text that is copied from the source
		1. TROUBLESOME: Manually copying and pasting text is not fast.
	3. Text in an image:
		1. TROUBLESOME: Navigating the OCR is slow and cumbersome.
2. By images:
	1. Images drawn by the user
		1. EASY: Can be done using Excalidraw
	2. Images copied from the source
		1. IMPOSSIBLE: Pasting images from source to Obsidian is impossible without add-ons.


#### Use Cases for Webcasts
1. By text:
	1. Summaries written by the user (PC, VERY EASY)
	2. Text that is copied from the source (PC, VERY EASY)
	3. Text in an image (PC, EASY)
2. By images:
	2. Images copied from the source (PC, VERY EASY)

#### Use Cases for Papers / Books
1. PDFs and their generated annotations are stored under pdfs:
	1. Unread: Papers that I've downloaded but not actually read.
	2. Read: Papers that I've read and intend to generate annotations for and subsequently automatically archive
	3. Archived: Papers that are automatically copied from the Read folder upon running `annotations_to_md.py`.
	4. Annotations: Generated markdown of extracted annotations (highlights & comments).
**Text & summaries:**
**OLD workflow involving Zotero**
1. Save the paper as a PDF in the Papers directory (Tablet, print to PDF if needed)
	1. This assumes you've setup some sort of multi-device sync for Obsidian. See [link](https://forum.obsidian.md/t/sync-mobile-app-through-google-drive-android-windows10/20891).
2. Highlight sections of the paper (Tablet). I use Xodo.
3. Add file to Zotero (PC) by clicking the green plus sign -> link to file -> select file in google drive.
	1. Assumes you have setup Zotero and related plugins: https://www.youtube.com/watch?v=_Fjhad-Z61o
	2. Other relevant info: https://forum.obsidian.md/t/zotero-best-practices/164/57	
4. Right click the PDF and select Manage Attachments -> Extract Annotations
5. With the annotations, Copy and paste, OR right click the extracted annotations and select Mdnotes -> Export to markdown.
6. If Zotero doesn't export the annotations, no choice, fallback to [pdf-highlights-extractor](https://sourceforge.net/projects/pdfhex/).
7. Port it into Obsidian.

**NEW workflow involving just 1 python script**
1. Save the paper as a PDF in the Papers/Read directory (Tablet, print to PDF if needed). 
2. Highlight sections of the paper (Tablet), add comments if you want. I use Xodo.
	1. If you want to crop a part of the PDF, include a comment '!img' on that page. I will generate a code snippet that leverages on Better PDF Plugin for you to fill in which part you want to crop.
3. Run `annotations_to_md.py`; it will save all annotations to md, and copy the PDF to the archived folder.
4. Once everything checks out, delete the PDF from the Read folder.

**Cropping images from PDFs**
1. Add an annotation to crop the image.
2. Later when converting to note, use Better PDF Plugin.

#### Use Cases for Articles / Websites
If the article / website is dense and contextualization will be helpful:
1. Convert the website into a PDF (Tablet, print to PDF)
2. Treat it as a paper

Otherwise:
1. Treat it as a webcast (PC)

https://forum.obsidian.md/t/zotero-best-practices/164/3