


from complex_domain.scrap_news.application.services.exceptions.exceptions import UrlNotFoundException
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import UrlRepositoryImpl


class UrlsAppService():

    def __init__(self) -> None:
        self.__url_reporitory = UrlRepositoryImpl()

    def get_urls(self):
        return self.__url_reporitory.get_all()

    def ignore_url(self, url_str):
        url = self.__url_reporitory.get_by_url(url_str)
        if url != None:
            url.ignored = True
            self.__url_reporitory.update(url)
        else:
            raise UrlNotFoundException("informed url's not found")

    