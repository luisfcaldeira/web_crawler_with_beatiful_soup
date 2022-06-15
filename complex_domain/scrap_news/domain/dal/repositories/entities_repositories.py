from abc import ABC, abstractmethod
from complex_domain.scrap_news.domain.entities.articles import Article

from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url


class UrlRepository(ABC):
    @abstractmethod
    def create(self, url: Url):
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self) -> Url:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def get_all_not_ignored(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, url: Url):
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError
    
    @abstractmethod
    def exists(self, url: Url):
        pass

class TargetUrlRepository(ABC):
    @abstractmethod
    def create(self, url: TargetUrl):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
        
    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def update(self, url: TargetUrl):
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError
    
    @abstractmethod
    def exists(self, url: TargetUrl):
        pass


class ArticlesRepository(ABC):
    @abstractmethod
    def create(self, article: Article):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
        
    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def update(self, article: Article):
        raise NotImplementedError
