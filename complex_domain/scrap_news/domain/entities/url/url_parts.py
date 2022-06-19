import re

class UrlProtocol():

    __value = "http"

    def __init__(self, url: str):
        self.__extract(url)
    
    def __extract(self, url):
        group = re.findall(pattern=self.pattern, string=url)
        if re.match(pattern=self.pattern, string=url):
            self.__value = group[0]

    @property
    def protocol(self):
        return self.__value

    @property
    def pattern(self):
        return r"([htps]{4,5})\:\/\/"


class UrlDomain():

    __value = ""
    __parts = []

    def __init__(self, url: str, id=None):
        self.__extract(url)
        
        self.__id = None
        if id != None and isinstance(id, int):
            self.__id = id

    @property
    def id(self) -> int:
        return self.__id
        
    @property
    def parts(self):
        return self.__parts

    @property
    def domain(self) -> str:
        return self.__value
    
    @property
    def pattern(self):
        return r"(?:http\:\/\/|https\:\/\/)?((?:[\w\d\-]{2,}\.)(?:[\w\d\-]{2,}\.?)(?:[\w\d\-]{2,}\.?)?(?:[\w\d\-]{2,}\.?)?(?:[\w\d\-]{2,}\.?)?(?:[\w\d\-]{2,}\.?)?(?:[\w\d\-]{2,}\.?)?)\/?[^\s]*"

    def __extract(self, url):
        group = re.findall(pattern=self.pattern, string=url)
        if len(group) > 0:
            self.__value = group[0]
            self.__parts = group[1:]
            self.__value = re.sub('^[w]{3}\.', '', self.__value)

    def __eq__(self, other):
        return isinstance(other, UrlDomain) and self.domain == other.domain

class IgnoredDomain(UrlDomain):
    def __repr__(self):
        return f"IgnoredDomain: {self.domain}"