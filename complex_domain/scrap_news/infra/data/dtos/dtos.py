
from abc import abstractmethod
import datetime
from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url
from peewee import *

db = SqliteDatabase('web_scrapper.db')

class Dto(Model):
    id = AutoField()
    class Meta:
        database = db 

    @abstractmethod
    def to_entity():
        pass

    @abstractmethod
    def from_entity(self, entity):
        pass

class UrlDto(Dto):
    url_str = CharField()
    domain = CharField()
    last_access = DateTimeField(default=datetime.datetime.now)
    ignored = BooleanField(default=False)

    def to_entity(self) -> Url:
        return Url(self.url_str, last_access=self.last_access)

    @staticmethod
    def from_entity(entity: Url):
        return UrlDto(url_str=entity.url, domain=entity.domain.domain, last_access=entity.last_access)

    
class TargetUrlDto(Dto):
    url_str = CharField()
    domain = CharField()

    def to_entity(self):
        return TargetUrl(url_str=self.url_str)

    @staticmethod
    def from_entity(entity: TargetUrl):
        return TargetUrlDto(url_str=entity.url, domain=entity.domain.domain)

db.connect()
db.create_tables([UrlDto, TargetUrlDto])