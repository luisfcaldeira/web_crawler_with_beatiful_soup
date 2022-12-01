


from complex_domain.scrap_news.application.services.exceptions.exceptions import UrlNotFoundException
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import UrlRepositoryImpl


class UrlsAppService():

    def __init__(self) -> None:
        self.__url_repository = UrlRepositoryImpl()

    def get_urls(self):
        return self.__url_repository.get_all()

    def ignore_url(self, url_str):
        url = self.__url_repository.get_by_url(url_str)
        if url != None:
            url.ignored = True
            self.__url_repository.update(url)
        else:
            raise UrlNotFoundException("informed url's not found")

    def save_url(self, url):
        target_url = Url(url)
        if not self.__url_repository.exists(target_url):
            self.__url_repository.create(url=target_url)

    