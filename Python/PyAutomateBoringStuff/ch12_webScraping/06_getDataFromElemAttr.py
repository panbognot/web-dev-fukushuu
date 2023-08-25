# We use select() to find any <span> elements and then store the first matched
# element in spanElem. Passing the attribute name 'id' to get() returns the
# attribute's value, 'author'.

import bs4 
from pathlib import Path 

# Just for checking if we are in the proper directory
p = Path.cwd()
print(p)

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]

print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)