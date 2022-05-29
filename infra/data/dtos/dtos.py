
from abc import abstractmethod
from domain.entities.urls import Url
from peewee import *

db = SqliteDatabase('web_scrapper.db')

class Dto(Model):

    class Meta:
        database = db 

    @abstractmethod
    def to_entity():
        pass

    @abstractmethod
    def from_entity(self, entity):
        pass

class UrlDto(Dto):
    id = AutoField()
    url_str = CharField()

    def to_entity(self) -> Url:
        return Url(self.url_str)

    @staticmethod
    def from_entity(entity: Url):
        return UrlDto(url_str=entity.url)

db.connect()
db.create_tables([UrlDto])