from bs4 import BeautifulSoup
import requests
import re


def getHTMLdocument(url):
    response = requests.get(url)
    return response.text
  
url_to_scrape = "https://g1.globo.com/"

html_document = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    print(link.get('href'))