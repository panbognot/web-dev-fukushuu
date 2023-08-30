#! python3
# google.py - google specific web scraper
# From: https://www.scrapingdog.com/blog/scrape-google-search-results/
# There are limitations to scraping google so be sure to check it out.
# Also, it is highly likely that you'll need to update this code since google
# often change their codes to prevent scraping.

import pprint
from bs4 import BeautifulSoup
import requests
from random import randrange

# For randomization of User Agent to prevent blocking from google
userAgents=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1']

headers={'User-Agent':userAgents[randrange(10)]}
url='https://www.google.com/search?q=pizza&amp;ie=utf-8&amp;oe=utf-8&amp;num=10'
html = requests.get(url,headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')
allData = soup.find_all("div", {"class":"MjjYud"})

g = 0
Data = []
l = {}
for i in range(0, 5):
  link = allData[i].find('a').get('href')

  if (link is not None):
    if (link.find('https') != -1 and link.find('http') == 0 and link.find('aclk') == -1):
      g = g + 1
      l["link"] = link

      # Find the title of the link
      try:
        l["title"] = allData[i].find('h3').text
      except:
        l["title"] = None

      # Find the description of the link (manually coded this)
      try:
        divDesc = allData[i].find("div", {"class": "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"})
        spanDescs = divDesc.find_all('span')
        l["description"] = ""
        for span in spanDescs:
          l["description"] = l["description"] + span.text
      except:
        l["description"] = None

      l["position"] = g 
      Data.append(l)
      l = {}

    else:
      continue
  else:
    continue

pprint.pprint(Data)