from abc import ABC, abstractmethod
import re
from infra.services.package_manager import PackageManager
from infra.services.strings_service import clear_string, fix_encoding

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    PackageManager.install('bs4')
    from bs4 import BeautifulSoup

from infra.services.web_document import Document

class CrawlerService(ABC):
    @abstractmethod
    def find_all_anchors(self):
        pass

class BSCrawlerService(CrawlerService):
    def __init__(self, document: Document) -> None:
        self.__document = document.get_document()
        self.__soup = BeautifulSoup(self.__document, 'html.parser')

    def get_all_anchors_address(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)

        attr_config['href'] = re.compile("^[htps]{4,5}\:\/\/")

        for link in w_element.find_all('a', attrs=attr_config):
            yield link.get('href')

    def get_all_p_content(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)

        for paragraph in w_element.find_all('p', attr_config):
            yield clear_string(paragraph)
    
    def find_all_div(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)

        for dv in w_element.find_all('div', attr_config):
            yield dv

    def __get_config(self, class_name, wrapper_element):
        attr_config = {}

        if class_name != None:
            attr_config = {'class' : class_name}

        w_element = self.__soup
        if wrapper_element != None:
            w_element = wrapper_element

        return attr_config, w_element