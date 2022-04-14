import re
from domain.exceptions.urls_exceptions import MalFormedUrlException
from domain.entities.url.url_parts import UrlProtocol, UrlDomain


class Url():
    __url_protocol = None
    __domain = None

    def __init__(self, url_str : str) -> None:
        self.__validar_url(url_str)
        self.__url_str = url_str
        self.__domain = UrlDomain(url_str)
        self.__url_protocol = UrlProtocol(url_str)

    def __validar_url(self, url_str : str):
        pattern = r"(?:http\:\/\/|https\:\/\/)?(?:[w.]{4})?([a-z]+)\.\b([a-z]+)?\.?([a-z]+)?"
        match = re.match(pattern, url_str)

        if match == None:
            raise MalFormedUrlException(f"Informed string is not a valid url: {url_str}")
        
    @property
    def url(self):
        return self.__url_str

    @property
    def protocol(self):
        return self.__url_protocol

    @property
    def domain(self):
        return self.__domain

