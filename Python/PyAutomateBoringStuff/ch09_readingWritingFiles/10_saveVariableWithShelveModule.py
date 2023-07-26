# You can save variable in your Python programs to binary shelf files
# using the "shelve" module. This way, your program can restore data
# to variables from the hard drive. The "shelve" module will let you
# add Save and Open features to your program.
# Ex. Configuration settings

# Shelf values don't have to be opened in read or write mode - they
# can do both once opened.

import shelve
from pathlib import Path

# Path of current chapter
p = Path('ch09_readingWritingFiles')

# CREATE AND STORE
# Create a shelf file and store data
shelfFile = shelve.open(p / 'mydata')
dogs = ['Kuma', 'Psyche', 'Mini', 'Phoebus']
shelfFile['dogs'] = dogs
shelfFile.close()

# OPEN AND LOAD
# Use the shelf module to open the shelf file and read the stored data
shelfFile = shelve.open(p / 'mydata')
# Display the file type. (Not really needed in practical apps)
type(shelfFile)
# Read the stored data
shelfFile['dogs']
shelfFile.close()

# Just like dictionaries, shelf values have keys() and values() that will
# return list-like values of the keys and values in the shelf.
# Pass them to the list() function to get them in list form
shelfFile = shelve.open(p / 'mydata')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()