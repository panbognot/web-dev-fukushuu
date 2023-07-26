# Path.exists() function is the equivalent of the older version
# os.path.exists(path), os.path.isfile(path), os.path.isdir(path)
# At least the Python 3.6 Path function works as a general purpose
# function to check regardless of file type

from pathlib import Path

cur = Path.cwd() / Path('ch03_functions')
notExistDir = cur / Path('this/folder/does/not/exist')
zigzagFile = cur / Path('11_zigzag.py')
dDrive = Path('D:/')
fDrive = Path('F:/')

# Use *.exists() function to check if the file or folder exists
cur.exists()
notExistDir.exists()
zigzagFile.exists()

# Check if the D drive or a flash drive exists
dDrive.exists()
fDrive.exists()