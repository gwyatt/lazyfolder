#!/usr/bin/python
from sys import argv
import os
import itertools

#Set up folders and sub-folders
mainfolders = [["01. Static","02. Animate","03. Assets"],
                ["01. MM&M","02. PM360","03. MedAdNews"],
                ["01. A", "02. B"],
                ["01. Text","02. Spreadsheets","03. Presentations","04. Other"]]

# Check for number of arguments
# Need at least one - starting folder name

if len(argv) == 1:
    print "Please Enter a folder name:\n"
    project = raw_input('> ')
else:
    project = argv[1]

try:
    os.makedirs(project)
    for item in itertools.product(*mainfolders):
        os.makedirs(project+"/"+os.path.join(*item))
except OSError:
    raise Exception("Folder Exists!")
