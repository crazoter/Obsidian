"""
split_pdf.py : Choose & extract pdf chunks from a pdf in the vault
I just named it split_pdf.py because I use it mainly for that purpose.
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.0"

import utils
utils.installMissingPackages({'pdfrw'})
ENV = utils.load_env(['ROOT'])
ROOT = ENV['ROOT']

from pdfrw import PdfReader, PdfWriter
from pathlib import Path

def getIntinput(prompt, lowerBoundExc, upperBoundExc, non_numeric_handler = None):
	val = -1
	valid = False
	while (not valid):
		print(prompt)
		val = input()
		if not val.isnumeric():
			if non_numeric_handler:
				non_numeric_handler(val)
				continue
			else:
				print("Invalid index input.")
				continue
		val = int(val)
		if val <= lowerBoundExc or val > upperBoundExc:
			print("Invalid index input.")
			continue
		valid = True
	return val

if __name__ == "__main__":
	# Req: Python 3.4+
	# https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python
	pdfs = list(Path(ROOT).rglob("*.[pP][dD][fF]"))
	prompt = f'List of PDFs found under root directory {ROOT}'
	print('=' * len(prompt))
	print(prompt)
	print('=' * len(prompt))
	for i in range(len(pdfs)):
		print(f'[{i+1}] {pdfs[i]}')
	if len(pdfs) <= 0:
		print("No PDFs found.")
		input("Press Enter to continue...")

	def non_numeric_handler(string):
		print(f'Searching pdfs that contain the string {string}')
		print('Results:')
		for i in range(len(pdfs)):
			if string.lower() in str(pdfs[i]).lower():
				print(f'[{i+1}] {pdfs[i]}')

	print('')
	idx = getIntinput("Select a PDF by index (input a string to perform a search): ", 0, len(pdfs), non_numeric_handler) - 1

	pdf = pdfs[idx]
	print(f'Extracting pdf {pdf}')
	pages = PdfReader(pdf).pages
	page_count = len(pages)
	print(f'PDF has {page_count} pages.')
	print('Beginning extraction. To exit, press CTRL-C.')
	while (True):
		part = [-1,-1]
		part[0] = getIntinput("1) Define first page of chunk (inclusive): ", 0, page_count)
		part[1] = getIntinput("2) Define last page of chunk (exclusive): ", 0, page_count)

		# https://stackoverflow.com/questions/55611121/split-specific-pages-of-pdf-and-save-it-with-python
		outfilename = str(pdf).replace('.pdf','')
		final_outfile = f'{outfilename}_pg_{part[0]}_{part[1]}.pdf'
		outdata = PdfWriter(final_outfile)
		for pagenum in range(*part):
			outdata.addpage(pages[pagenum-1])
		outdata.write()
		print(f'Generated PDF {final_outfile}.')
		print('Continuing extraction. To exit, press CTRL-C.')