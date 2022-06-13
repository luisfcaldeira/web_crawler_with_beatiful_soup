
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import TargetsUrlRepositoryImpl, UrlRepositoryImpl
from complex_domain.scrap_news.infra.services.web_document import WebDocument
from complex_domain.scrap_news.services.web_crawler.folha_crawler_service import FolhaCrawlerService


class ScrapAppService():

    def __init__(self) -> None:
        self.__url_repository = UrlRepositoryImpl()
        self.__targets_repository = TargetsUrlRepositoryImpl()

    def run(self):
        targets = self.__convert_targets_into_urls()

        urls = self.__url_repository.get_all_not_ignored()

        for url in urls:
            self.__run_url(targets, url) 

    def __convert_targets_into_urls(self):
        targets = self.__targets_repository.get_all()
        urls = []
        for target in targets:
            target_url = Url(target.url_str)
            
            if not self.__url_repository.exists(target_url):
                self.__url_repository.create(url=target_url)

            urls.append(self.__url_repository.get_by_url(target.url_str)[0])

        return urls

    def __run_url(self, targets, url):
        print(f"accessing {url.url_str}")

        try:
            document = WebDocument(url.url_str)
            folha_crawler = FolhaCrawlerService(document)
            anchors = folha_crawler.get_all_anchors_address()
            self.__collect_anchors(targets, anchors)  

        except Exception as e:
            url.ignored = True
            url.error = e
            self.__url_repository.update(url=url)

    def __collect_anchors(self, targets, anchors):
        for anchor in anchors:
            new_url = Url(anchor)

            if new_url not in targets:
                new_url.ignored = True
            
            print(new_url.url_str, " - ignored: ", new_url.ignored)

            if not self.__url_repository.exists(new_url):
                print('creating:', new_url)
                self.__url_repository.create(url=new_url)
            else:
                print('updating:', new_url)
                self.__url_repository.update(url=new_url)
