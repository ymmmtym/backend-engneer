import requests
import os
import sys
from bs4 import BeautifulSoup


def scraping(url):
  r = requests.get(url)
  text = r.text
  content = r.content
  soup = BeautifulSoup(content, 'html.parser')
  return soup.title


if __name__ == "__main__":
    print(scraping(sys.argv[1]))
