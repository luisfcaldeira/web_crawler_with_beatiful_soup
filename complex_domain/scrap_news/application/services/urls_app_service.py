


from complex_domain.scrap_news.infra.data.repositories.entities_repositories import UrlRepositoryImpl


class UrlsAppService():

    def __init__(self) -> None:
        self.__url_reporitory = UrlRepositoryImpl()

    def get_urls(self):
        return self.__url_reporitory.get_all()