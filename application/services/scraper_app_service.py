
from domain.entities.urls import Url
from infra.services.web_document import Document, WebDocument
from services.web_crawler.beautiful_soup import BSCrawlerService
from services.web_crawler.folha_crawler_service import FolhaCrawlerService


class ScrapAppService():

    def run(self, url: Url):
        document = WebDocument(url.url)
        folha_crawler = FolhaCrawlerService(document)
        print(folha_crawler.get_news())