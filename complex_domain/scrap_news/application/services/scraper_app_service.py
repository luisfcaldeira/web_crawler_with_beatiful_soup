
from complex_domain.scrap_news.application.services.urls_targets_app_service import UrlsTargetsAppService
from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import TargetsUrlRepositoryImpl, UrlRepositoryImpl
from complex_domain.scrap_news.infra.services.web_document import Document, WebDocument
from complex_domain.scrap_news.services.web_crawler.beautiful_soup import BSCrawlerService
from complex_domain.scrap_news.services.web_crawler.folha_crawler_service import FolhaCrawlerService


class ScrapAppService():

    def __init__(self) -> None:
        self.__url_repository = UrlRepositoryImpl()
        self.__targets_repository = TargetsUrlRepositoryImpl()
        self.__urls_targets_app_service = UrlsTargetsAppService()

    def run(self):
        target_folha = TargetUrl("https://www.folha.uol.com.br/")

        if not self.__targets_repository.exists(target_folha):
            self.__targets_repository.create(target_folha)

        url = Url("https://www1.folha.uol.com.br/poder/2022/05/bolsonaro-dobra-numero-de-viagens-em-2022-e-acumula-eventos-com-perfil-eleitoral.shtml")

        document = WebDocument(url.url)
        folha_crawler = FolhaCrawlerService(document)
        
        if not self.__url_repository.exists(url):
            self.__url_repository.create(url=url)

        targets = self.__urls_targets_app_service.get_all()
        print(targets)
        anchors = folha_crawler.get_all_anchors_address()

        for anchor in anchors:

            new_url = Url(anchor)
            if not new_url.domain.domain in targets:
                new_url.ignored = True

            if not self.__url_repository.exists(new_url):
                self.__url_repository.create(url=new_url)
            else:
                self.__url_repository.update(url=new_url)

                print(new_url.domain.domain, '-', new_url.url_str)
