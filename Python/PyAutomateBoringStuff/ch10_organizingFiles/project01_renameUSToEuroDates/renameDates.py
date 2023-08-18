#! python3
# Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re 
from pathlib import Path

projPath = Path.cwd() / 'ch10_organizingFiles/project01_renameUSToEuroDates'

# print(os.getcwd())
# os.chdir('./ch10_organizingFiles/project01_renameUSToEuroDates')
# print(os.getcwd())

# Create a regex that matches file with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
  ((0|1)?\d)-                       # one or two digits for the month
  ((0|1|2|3)?\d)-                   # one or two digits for the day
  ((19|20)\d\d)                     # four digits for the year
  (.*?)$                            # all text after the date
  """, re.VERBOSE)

# Loop over the files in the working directory.
# for amerFilename in os.listdir('.'):
for amerFilename in projPath.iterdir():
  # mo = datePattern.search(amerFilename)
  mo = datePattern.search(str(amerFilename))

  # Skip files without a date.  
  if mo == None:
    continue

  # Get the different parts of the filename.
  beforePart  = mo.group(1)
  monthPart   = mo.group(2)
  dayPart     = mo.group(4)
  yearPart    = mo.group(6)
  afterPart   = mo.group(8)
  
  # The group numbers are based on the number of open parenthesis.
  # datePattern = re.compile(r"""^(1) # all text before the date
  #   (2 (3) )-                     # one or two digits for the month
  #   (4 (5) )-                     # one or two digits for the day
  #   (6 (7) )                      # four digits for the year
  #   (8)$                          # all text after the date
  #   """, re.VERBOSE)

  # Form the European-style filename.
  euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

  # Get the full, absolutte file pathss.
  # absWorkingDir = os.path.abspath('.')
  # amerFilename = os.path.join(absWorkingDir, amerFilename)
  # euroFilename = os.path.join(absWorkingDir, euroFilename)

  # Rename the files.
  print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
  # shutil.move(amerFilename, euroFilename) # uncomment after testing