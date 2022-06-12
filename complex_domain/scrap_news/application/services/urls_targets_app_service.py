

from complex_domain.scrap_news.domain.entities.urls import TargetUrl
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import TargetsUrlRepositoryImpl


class UrlsTargetsAppService():

    def __init__(self) -> None:
        self.__targets_repository = TargetsUrlRepositoryImpl()

    def add_new_target(self, url: str) -> None:
        target_folha = TargetUrl(url)

        if not self.__targets_repository.exists(target_folha):
            self.__targets_repository.create(target_folha)
    
    def get_all_str_domain(self) -> list():
        result = self.__targets_repository.get_all()
        return [e.domain for e in result]
