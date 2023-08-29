#! python3
# Got this code pattern at: 
# https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/#querying-the-dom

import pprint
import webbrowser
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
if response.status_code != 200:
  print("Error fetching page")
  exit()

soup = BeautifulSoup(response.content, 'html.parser')
# I manually looked for the structure to get the hyperlinks of each news
links = soup.select('.titleline > a')
# pprint.pprint(links)

# Open 5 links on the web browser
numOpen = min(5, len(links))
for i in range(numOpen):
  urlToOpen = links[i].get('href')
  print('Opening', urlToOpen)
  webbrowser.open(urlToOpen)