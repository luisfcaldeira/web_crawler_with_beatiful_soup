
from abc import abstractmethod
import datetime
from complex_domain.scrap_news.domain.entities.articles import Article
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
    discovered_at = DateTimeField(default=datetime.datetime.now())
    last_access = DateTimeField(null=True)
    ignored = BooleanField(default=False)
    error = CharField(null=True)

    def to_entity(self) -> Url:
        url = Url(self.url_str)
        url.id = self.id
        url.last_access = self.last_access
        url.discovered_at = self.discovered_at
        url.error = self.error
        url.ignored = self.ignored

        return url

    @staticmethod
    def from_entity(entity: Url):
        url_dto = UrlDto(id=entity.id, \
                        url_str=entity.url, \
                        domain=entity.domain.domain, \
                        last_access=entity.last_access, \
                        discovered_at=entity.discovered_at, \
                        ignored=entity.ignored
                        )
        
        return url_dto

                
class TargetUrlDto(Dto):
    url_str = CharField()
    domain = CharField()

    def to_entity(self):
        return TargetUrl(url_str=self.url_str, id=self.id)

    @staticmethod
    def from_entity(entity: TargetUrl):
        return TargetUrlDto(id=entity.id, url_str=entity.url, domain=entity.domain.domain)

class ArticleDto(Dto):
    title = CharField(default="", null=True)
    date = DateTimeField(null=True)
    section = CharField(default="", null=True)
    text = CharField()
    url = ForeignKeyField(UrlDto)

    def to_entity(self):
        return Article(id=self.id, title=self.title, date=self.date, section=self.section, text=self.text, url=self.url.id)

    @staticmethod
    def from_entity(entity: Article):
        return ArticleDto(id=entity.id, title=entity.title, date=entity.date, section=entity.section, text=entity.text, url=entity.url.id)


db.connect()
db.create_tables([UrlDto, TargetUrlDto, ArticleDto])

