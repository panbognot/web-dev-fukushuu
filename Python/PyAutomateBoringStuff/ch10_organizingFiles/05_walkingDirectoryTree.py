import os
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles/cuties'

for folderName, subfolders, filenames in os.walk(p):
  print('The current folder is ' + folderName)

  for subfolder in subfolders:
    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

  for filename in filenames:
    print('FILE INSIDE ' + folderName + ': ' + filename)

  print('')