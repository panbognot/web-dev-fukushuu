import shutil, os
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'

# Copy the file into a folder and retain the filename
shutil.copy(p / 'pets.txt', p / 'test_folder')
# Copy the file and rename it
shutil.copy(p / 'kuma.txt', p / 'test_folder/cute.txt')

# Copy a whole folder
shutil.copytree(p / 'test_folder', p / 'bkp_folder')