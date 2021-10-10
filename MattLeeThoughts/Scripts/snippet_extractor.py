#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
snippet_extractor.py : Search obsidian vault for snippets and creates files for them.

This script will scan for .md files starting from the root directory (recursively searching subfolders) .
It expects the same syntax provided by the [[Using text snippets]] template. You can see a few examples e.g. [[Python General]] in the Snippets folder.
Essentially, whenever this script encounters '#region SNIPPET' it will start collecting lines, and stops after encountering '#endregion'. 
For this reason, refrain from using '#endregion' in your snippets.
It will then use the string stored by the tabTrigger and scope tags to generate a file containing the snippet in the sublime text snippet directory.
"""

__author__ = "Matt Lee"
__copyright__ = "Copyright 2021, crazoter"
__license__ = "GPL 3.0"
__version__ = "1.0.0"

from pathlib import Path
import re
# https://docs.python.org/3/library/enum.html
# e.g. Color.RED
from enum import Enum
class State(Enum):
	INACTIVE = 1
	READ_BASIC = 2 # Basic includes the snippet template.
	READ_SHORT = 3 # Short removes the snippet template, replacing it with a more readable version in the markdown.

# Install required dependencies if not already installed
# https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
import sys
import subprocess
import pkg_resources

required = {"python-dotenv"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Installing missing required dependencies...")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# Load variables from environment file
# Requires python-dotenv
# https://stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file
import os
from dotenv import load_dotenv
# .env file contains MY_ENV_VAR="This is my env var content."
load_dotenv()
ENV = {
	"ROOT" : os.getenv("ROOT"),
	"SUBLIME_TEXT_SNIPPET_DIR" : os.getenv("SUBLIME_TEXT_SNIPPET_DIR"),
}
for key in ENV:
	if ENV[key] == None:
		print(f"Error: {key} is not defined (is there a .env file in the directory?)")
		print(f"The .env file should contain '{key} = someValue,SeeDocumentation'")
		input("Press Enter to continue...")
		exit()

ROOT = ENV['ROOT']
SUBLIME_TEXT_SNIPPET_DIR = ENV['SUBLIME_TEXT_SNIPPET_DIR']
VERBOSE = True

def write_to_file(scope, tab_trigger, collected_lines):
	outfile = scope + "-" + tab_trigger
	if len(outfile) > 1:
		outfilename = f"{SUBLIME_TEXT_SNIPPET_DIR}{outfile}.sublime-snippet"
		if VERBOSE:
			print("Writing to " + outfilename)
		with open(outfilename, 'w') as outfp:
			outfp.writelines(collected_lines)


if __name__ == "__main__":
	# https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python
	for filename in Path(ROOT).rglob("*.[mM][dD]"):
		if VERBOSE:
			print("Opened " + str(filename))
		with open(filename, 'r', errors='replace') as fp:
			tab_trigger = ""
			scope = ""

			collected_lines = []
			current_state = State.INACTIVE
			for line in fp:
				# Depending on the state, interpret the line differently.
				if current_state is State.READ_BASIC:

					if line.strip() == '#endregion':
						current_state = State.INACTIVE
						write_to_file(scope, tab_trigger, collected_lines)
						collected_lines = []
						continue

					collected_lines.append(line)

					regex_search = re.search('<tabTrigger>(.+)</tabTrigger>', line, re.IGNORECASE)
					if regex_search:
					    tab_trigger = regex_search.group(1)

					regex_search = re.search('<scope>(.+)</scope>', line, re.IGNORECASE)
					if regex_search:
					    scope = regex_search.group(1)
				if current_state is State.READ_SHORT:
					if line.strip() == '```':
						current_state = State.INACTIVE
						collected_lines.append(f"]]></content><tabTrigger>{tab_trigger}</tabTrigger>")
						collected_lines.append(f"<scope>{scope}</scope></snippet>")
						write_to_file(scope, tab_trigger, collected_lines)
						collected_lines = []
						continue
					else:
						collected_lines.append(line)

				elif '#region SNIPPET' in line.strip():
					current_state = State.READ_BASIC
				elif '#region SHORTSNIPPET' in line.strip():
					current_state = State.READ_SHORT
					data = line.split('|')
					scope = data[1].strip()
					tab_trigger = data[2].strip()
					collected_lines.append("<snippet><content><![CDATA[")