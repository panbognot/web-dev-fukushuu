import bs4
from pathlib import Path

# Just for checking if we are in the proper directory
p = Path.cwd()
print(p)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

# Select the ID author
elems = exampleSoup.select('#author')

print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)

# Select ALL <p> elements
pElems = exampleSoup.select('p')

print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())