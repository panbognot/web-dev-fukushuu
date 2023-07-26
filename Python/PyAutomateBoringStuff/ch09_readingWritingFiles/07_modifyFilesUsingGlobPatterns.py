# If you want to perform some operation on every file in a directory, you can
# use either os.listdir(p) or p.glob('*').

from pathlib import Path

p = Path.cwd()
relPath = p / Path('ch03_functions')

# Make a list from the generator.
list(p.glob('*'))

# Lists all python files in the folder
list(relPath.glob('*.py'))

# Lists python files with the pattern '*Name*.?y'
list(relPath.glob('*Name*.?y'))

# Use a loop to iterate over the generator the glob() returns
for textFilePathObj in relPath.glob('*Name*.py'):
  print(textFilePathObj)  # Prints the Path object as string