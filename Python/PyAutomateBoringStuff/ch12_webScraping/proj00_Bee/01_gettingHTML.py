import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
if response.status_code != 200:
  print("Error fetching page")
  exit()
else:
  content = response.content

print(content)

soup = BeautifulSoup(response.content, 'html.parser')
# The title tag of the page
print(soup.title)
# The title of the page as string
print(soup.title.string)

# All links in the page
nb_links = len(soup.find_all('a'))
print(f"There are {nb_links} links in this page")

# Text from the page
print(soup.get_text())