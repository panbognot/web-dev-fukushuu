import requests
from bs4 import BeautifulSoup
from collections import Counter

response = requests.get("https://news.ycombinator.com")
if response.status_code != 200:
  print("Error fetching page")
  exit()

soup = BeautifulSoup(response.content, 'html.parser')
first_link = soup.a 
print(first_link)
# The text of the link
print(first_link.text)
# The href of the link
print(first_link.get('href'))

pagespace = soup.find(id="pagespace")
print(pagespace)

# class is a reserved keyword in Python, hence the '_'
athing = soup.find(class_="athing")
print(athing)

all_hrefs = [a.get('href') for a in soup.find_all('a')]
top_3_links = Counter(all_hrefs).most_common(3)
print(top_3_links)