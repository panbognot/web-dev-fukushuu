from pathlib import Path
import os

# Check if the path is absolute
Path.cwd()
print('Is Path.cwd().is_absolute()?')
print(Path.cwd().is_absolute())
print("Is Path('spam/bacon/eggs').is_absolute()?")
print(Path('spam/bacon/eggs').is_absolute())

# Use path joins to create an absolute path
print("Is Path.cwd() / Path('my/relative/path').is_absolute()?")
print((Path.cwd() / Path('my/relative/path')).is_absolute())

# Using the os library instead for absolute paths
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print("Is os.path.isabs('.') absolute?")
print(os.path.isabs('.'))
print("Is os.path.isabs(os.path.abspath('.')) absolute?")
print(os.path.isabs(os.path.abspath('.')))

# Using the os library for relative paths
print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))