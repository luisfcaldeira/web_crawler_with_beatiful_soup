from domain.entities.urls import Url
from infra.services.package_manager import PackageManager
from infra.services.web_document import MockWebDocument, WebDocument
from services.web_crawler.beautiful_soup import BSCrawler

url = Url("http://www.teste.com.br")
url2 = Url("http://www.teste.com.br")

print(url.domain.domain)
print(url == url2)
print(url == 'url2')


try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    PackageManager.install('bs4')

try:
    import requests
except ModuleNotFoundError:
    PackageManager.install('requests')

bs_crawler = BSCrawler(MockWebDocument("https://g1.globo.com/"))

bs_crawler.find_all_anchors()