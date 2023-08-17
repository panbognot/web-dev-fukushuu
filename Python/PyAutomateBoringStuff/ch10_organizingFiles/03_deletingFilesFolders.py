import os
from pathlib import Path
import shutil

p = Path.cwd() / 'ch10_organizingFiles'
pbkp = p / 'bkp_folder'

# os.unlink(path) will delete the file at path
# os.rmdir(path) will delete the folder at path
# shutil.rmtree(path) will remove the folder and all files at path

# for filename in p.glob('*.txt'):
  # os.unlink(filename)
  # print(filename)

shutil.rmtree(pbkp)