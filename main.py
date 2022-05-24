# https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/#:~:text=Use%20the%20a%20tag%20to,passing%20title%20argument%20to%20it.

from domain.entities.urls import Url
from infra.services.package_manager import PackageManager
from infra.services.web_document import MockWebDocument, WebDocument
from services.web_crawler.beautiful_soup import BSCrawlerService

url = Url("http://www.teste.com.br")
url2 = Url("http://www.teste.com.br")

print(url.domain.domain)
print(url == url2)
print(url == 'url2')


bs_crawler = BSCrawlerService(WebDocument("https://g1.globo.com/"))

anchors = list(bs_crawler.find_all_anchors())

for anchor in anchors:
    print(anchor)


'''

    Criar application service para retornar urls 
    Regra para preparar URL para analise 
    Regra para avaliar se o URL deve ser analisada novamente 

'''