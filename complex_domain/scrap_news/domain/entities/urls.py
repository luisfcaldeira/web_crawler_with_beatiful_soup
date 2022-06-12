import datetime
import re
from complex_domain.scrap_news.domain.exceptions.urls_exceptions import MalFormedUrlException
from complex_domain.scrap_news.domain.entities.url.url_parts import UrlProtocol, UrlDomain


class Url():
    __url_protocol = None
    __domain = None

    def __init__(self, url_str : str, last_access = None) -> None:
        self.__check(url_str)
        self.url_str = url_str
        self.__domain = UrlDomain(url_str)
        self.__last_access = datetime.datetime.now()
        self.__url_protocol = UrlProtocol(url_str)
        self.__ignored = False

        if last_access != None and isinstance(last_access, datetime.datetime):
            self.__last_access = last_access

    def __check(self, url_str : str):
        pattern = r"(?:http\:\/\/|https\:\/\/)?([\w\d\-]{2,}\.)([\w\d\-]{2,}\.?)([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?\/?[^\s]*"
        match = re.match(pattern, url_str)

        if match == None:
            raise MalFormedUrlException(f"Informed string is not a valid url: {url_str}.")
        
    @property
    def url(self):
        return self.url_str

    @property
    def protocol(self):
        return self.__url_protocol

    @property
    def domain(self):
        return self.__domain

    @property
    def last_access(self):
        return self.__last_access
    
    @last_access.setter
    def last_access(self, value):
        self.__last_access = value

    @property
    def is_ignored(self):
        return self.__ignored

    @is_ignored.setter
    def ignored(self, value):
        if isinstance(value, bool):
            self.__ignored = value

    def update_last_access(self):
        self.last_access = datetime.datetime.now()

    def __eq__(self, other):
        return isinstance(other, Url) and self.__domain == other.__domain


class TargetUrl(Url):
    pass