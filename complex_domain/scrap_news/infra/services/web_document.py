
from complex_domain.scrap_news.infra.services.package_manager import PackageManager
from abc import ABC, abstractmethod


try:
    import requests
except ModuleNotFoundError:
    PackageManager.install('requests')
    import requests

class Document(ABC):

    @property
    def url(self):
        return self.__url

    def __init__(self, url : str) -> None:
        super().__init__()
        self.__url = url
        
    @abstractmethod
    def get_document(self) -> str:
        pass


class WebDocument(Document):
    
    def get_document(self) -> str:
        '''
        return pure text html
        '''
        
        response = requests.get(super().url)
        return response.text
