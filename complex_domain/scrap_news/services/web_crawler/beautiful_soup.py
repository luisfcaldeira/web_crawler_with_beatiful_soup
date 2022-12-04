from abc import ABC, abstractmethod
import re
from complex_domain.scrap_news.infra.services.strings_service import clear_string
from complex_domain.scrap_news.infra.services.web_document import Document
from bs4 import BeautifulSoup

class CrawlerService(ABC):
    @abstractmethod
    def find_a(self, class_name=None, wrapper_element=None):
        pass

    @abstractmethod
    def get_all_anchors_address(self):
        pass

    @abstractmethod
    def get_div_by_property(self, property_name, property_value):
        pass

class BSCrawlerService(CrawlerService):

    def __init__(self, document: Document) -> None:
        self.__document = document.get_document()
        self.__soup = BeautifulSoup(self.__document, 'html.parser')

    def get_all_anchors_address(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)

        attr_config['href'] = re.compile("^[htps]{4,5}\:\/\/")
        addresses = []
        
        for link in w_element.find_all('a', attrs=attr_config):
            addresses.append(link.get('href'))

        return addresses

    def find_a(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)
        return w_element.find_all('a', attr_config)
        
    def get_all_p_content(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)
        texts = ''
        for paragraph in w_element.find_all('p', attr_config):
            if paragraph != None:
                texts += (clear_string(paragraph.text))
        return texts
        
    def find_all_div(self, class_name=None, wrapper_element=None):
        attr_config, w_element = self.__get_config(class_name, wrapper_element)
        divs = []
        for dv in w_element.find_all('div', attr_config):
            divs.append(dv)
        return divs

    def get_div_by_property(self, property_name, property_value):
        divs = []
        for dv in self.__soup.find_all('div', { property_name : property_value }):
            divs.append(dv)
        return divs

    def get_meta(self, property):
        attrs = {
            'property' : property
        }
        result = self.__soup.find("meta", attrs=attrs)
        if result != None and result.has_key('content'):
            return result.attrs['content']
        return None
    
    def get_title(self):
        result = self.__soup.find("title").text
        if result != None:
            return result
        return None

    def __get_config(self, class_name, wrapper_element):
        attr_config = {}

        if class_name != None:
            attr_config = {'class' : class_name}

        w_element = self.__soup
        if wrapper_element != None:
            w_element = wrapper_element

        return attr_config, w_element