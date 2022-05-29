from abc import ABC, abstractmethod

from domain.entities.urls import Url


class UrlRepository(ABC):
    @abstractmethod
    def create(self, url: Url):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def update(self, url: Url):
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError