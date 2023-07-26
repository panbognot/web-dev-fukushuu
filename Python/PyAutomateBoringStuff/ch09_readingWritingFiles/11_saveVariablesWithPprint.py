import pprint 
from pathlib import Path

p = Path.cwd() / 'ch09_readingWritingFiles'
pets = [{'name': 'Kuma', 'breed': 'Dutch Shepherd Mix'}, 
        {'name': 'Shiro', 'breed': 'Khao Manee'}, 
        {'name': 'Psyche', 'breed': 'Dachshund'},
        {'name': 'Mini', 'breed': 'Dachshund Husky Mix'},
        {'name': 'Phoebus', 'breed': 'Mongrel'}]

# Pretty print the dictionary
pprint.pformat(pets)

# Open a python file and write the variable there
fileObj = open(p / 'myPets.py', 'w')
fileObj.write('pets = ' + pprint.pformat(pets) + '\n')
fileObj.close()