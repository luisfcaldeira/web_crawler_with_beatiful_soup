from abc import ABC, abstractmethod

from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url


class UrlRepository(ABC):
    @abstractmethod
    def create(self, url: Url):
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int):
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
    def get_all_url(self):
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