#!/usr/bin/python
from sys import argv
import os

#Set up folders and sub-folders
mainfolders = ["01. Specifications","02. References","03. Assets","04. Documents"]

assets = ["01. PSDs et. al.",
			"02. Rendered Images",
			"03. Scripts"]

documents = ["01. Text",
			"02. Spreadsheets",
			"03. Presentations",
			"04. Other"]

# Check for number of arguments
# Need at least one - starting folder name

if len(argv) == 1:
	print "Please Enter a folder name:\n"
	path = raw_input('> ')
else:
	path = argv[1]

try:
	os.makedirs(path)
	for i, b in enumerate(mainfolders):
		os.makedirs(path+"/"+mainfolders[i])
except OSError:
	raise Exception("Folder Exists!")
