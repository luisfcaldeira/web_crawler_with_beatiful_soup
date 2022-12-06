import datetime
import re
from complex_domain.scrap_news.domain.entities.url.url_parts import UrlProtocol, UrlDomain



class Url():
    __url_protocol = None
    __domain = None

    def __init__(self, url_str: str, id=None) -> None:
        url_str = str(url_str)
        self.__check(url_str)
        self.url_str = url_str
        self.__domain = UrlDomain(url_str)
        self.__url_protocol = UrlProtocol(url_str)
        self.__discovered_at = datetime.datetime.now()
        self.__last_access = None
        self.__viewed = False
        self.__ignored = False
        self.__error = None
        self.__id = id

    def __check(self, url_str : str):
        pattern = r"(?:http\:\/\/|https\:\/\/)?([\w\d\-]{2,}\.)([\w\d\-]{2,}\.?)([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?([\w\d\-]{2,}\.?)?\/?[^\s]*"
        self.valid = False
        
        try :
            match = re.match(pattern, url_str)
                
            if match != None:
                self.valid = True

        except Exception as e:
            self.__error = e
        
    @property
    def url(self):
        if not ("http" in self.url_str):
            return f"http://{self.url_str}"
        return self.url_str

    def is_accepted(self, rule: dict):
        result = True
        if 'pattern' in rule:
            pttrn = rule['pattern']
            re_result = re.match(pttrn, self.url_str)
            result = result and re_result != None

        if 'contains' in rule:
            result = result and rule['contains'] in self.url_str

        return result

    def visit(self): 
        self.last_access = datetime.datetime.now()
        self.viewed = True

    @property
    def protocol(self):
        return self.__url_protocol

    @property
    def domain(self):
        return self.__domain

    @property
    def discovered_at(self):
        return self.__discovered_at
    
    @discovered_at.setter
    def discovered_at(self, value: datetime.datetime):
        if isinstance(value, datetime.datetime):
            self.__discovered_at = value
        
    @property
    def last_access(self):
        return self.__last_access
    
    @last_access.setter
    def last_access(self, value):
        if isinstance(value, datetime.datetime):
            self.__last_access = value
        else:
            self.__last_access = datetime.datetime.now()

    @property
    def is_ignored(self):
        return self.__ignored

    @is_ignored.setter
    def ignored(self, value):
        if isinstance(value, bool):
            self.__ignored = value

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        self.__error = str(value)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self.__id = value
    
    @property
    def viewed(self):
        return self.__viewed

    @viewed.setter
    def viewed(self, value):
        if isinstance(value, bool):
            self.__viewed = value

    def contains(self, domain: UrlDomain):
        return self.url_str.find(domain.domain) >= 0

    def update_last_access(self):
        self.last_access = datetime.datetime.now()
 
    def __repr__(self):
        return f"Url: {self.url_str} [Ignored:{self.ignored}]"

    def __eq__(self, other):
        return isinstance(other, Url) and self.url_str == other.url_str
    
    def __str__(self):
        return self.url_str
   
class TargetUrl(Url):
    def __repr__(self):
        return f"TargetUrl: {self.url_str}"

class UrlCollection(list):
    
    def exclude(self, urls):
        return UrlCollection([url for url in urls if url not in self])


