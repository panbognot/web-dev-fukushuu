# Write a program that opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. The results should
# be printed to the screen.
# Usage: py regExSearch.py <folder path>
from ast import Not
from genericpath import isfile
from pathlib import Path
from pickle import NONE
import sys
import pyinputplus as pyip

p = None

# If there is an argument, use that as the folder path
if len(sys.argv) == 2:
  p = Path.cwd() / sys.argv[1]
# the default folder input is the current working directory
else:
  p = Path()

# Create a user-supplied regular expression to be used for searching the folder
userRegex = pyip.inputRegexStr("Enter your regular expression for searching:\n", limit=3)

# Open all files inside the directory and search it using the RegEx
for item in p.iterdir():
  if item.is_file():
    print(str(item) + '\n')
    fd = open(p / item)
    baseContent = fd.readlines()
    fd.close()

    # Read the file per line and search the regex
    for line in baseContent:
      # print(line)
      mo = userRegex.findall(line)
      if mo != []:
        print(mo)