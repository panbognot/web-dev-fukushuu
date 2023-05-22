from pathlib import Path
import os

# Get the current working directory
print(Path.cwd())

# Make directories inside the CWD using relative paths
os.makedirs('./testA')
Path(r'./testB').mkdir()

# Change the current working directory
os.chdir('C:/Users/Admin/Documents')
print(Path.cwd())

# Get the home directory
print(Path.home())

