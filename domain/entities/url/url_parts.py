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

    def __init__(self, url: str):
        self.__extract(url)

    @property
    def domain(self):
        return self.__value
    
    @property
    def value(self):
        return self.__value

    @property
    def pattern(self):
        return r"((?:(w{3}|\w\d*)(?:\.))?(\w+)\.\b(\w{3,})?\.?(\w{0,2})?)"

    def __extract(self, url):
        group = re.findall(pattern=self.pattern, string=url)
        if len(group) > 0:
            self.__value = group[0][0]

    def __eq__(self, other):
        return isinstance(other, UrlDomain) and self.domain == other.domain
