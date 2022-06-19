

from complex_domain.scrap_news.domain.dal.repositories.entities_repositories import IgnoredDomainRepository
from complex_domain.scrap_news.domain.entities.url.url_parts import UrlDomain


class DomainAppService():

    def __init__(self, ignored_domain_repository: IgnoredDomainRepository) -> None:
        
        if not isinstance(ignored_domain_repository, IgnoredDomainRepository):
            raise Exception('make sure you are passing a subclass of IgnoredDomainRepository')
        self.__ignored_domain_repository = ignored_domain_repository

    def ignore_domain(self, url_str):
        domain = UrlDomain(url_str)
        self.__ignored_domain_repository.create(domain)