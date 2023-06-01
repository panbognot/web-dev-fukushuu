import os
from pathlib import Path

# Parts of a Path
p = Path.cwd()
print('Get size of path: %s' % (os.path.getsize(p)))
print('list: %s' % (os.listdir(p)))

# Get total size of the files in the folder
totalSize = 0
for filename in os.listdir(p):
  totalSize = totalSize + os.path.getsize(p / filename)
print('Total size of files inside folder: %s' % totalSize)