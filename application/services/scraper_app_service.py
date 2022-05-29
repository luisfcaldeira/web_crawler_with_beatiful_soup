
from domain.entities.urls import Url
from infra.data.repositories.entities_repositories import UrlRepositoryImpl
from infra.services.web_document import Document, WebDocument
from services.web_crawler.beautiful_soup import BSCrawlerService
from services.web_crawler.folha_crawler_service import FolhaCrawlerService


class ScrapAppService():

    def run(self, url: Url):
        
        document = WebDocument(url.url)
        folha_crawler = FolhaCrawlerService(document)
        repo = UrlRepositoryImpl()
        repo.create(url=url)
        # print(folha_crawler.get_news())