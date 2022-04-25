from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import re

from infra.services.web_document import Document

class Crawler(ABC):
    @abstractmethod
    def find_all_anchors(self):
        pass

class BSCrawler(Crawler):
    def __init__(self, document: Document) -> None:
        self.__document = document.get_document()

    def find_all_anchors(self):
        soup = BeautifulSoup(self.__document, 'html.parser')

        for link in soup.find_all('a', attrs={'href': re.compile("^[htps]{4,5}\:\/\/")}):
            yield link.get('href')