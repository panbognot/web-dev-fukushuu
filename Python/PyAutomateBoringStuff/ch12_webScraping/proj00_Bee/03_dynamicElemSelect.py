from urllib import response
import requests
from bs4 import BeautifulSoup
import re 

def my_tag_selector(tag):
  # We only accept "a" tags with a titlelink class
  return tag.name == "span" and tag.has_attr("class") and "titleline" in tag.get("class")

response = requests.get("https://news.ycombinator.com/")
if response.status_code != 200:
  print("Error fetching page")
  exit()

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.find_all(my_tag_selector))