from complex_domain.scrap_news.domain.dal.repositories.entities_repositories import IgnoredDomainRepository, TargetUrlRepository, UrlRepository, ArticlesRepository
from complex_domain.scrap_news.domain.entities.articles import Article
from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url, UrlCollection
from complex_domain.scrap_news.infra.data.dtos.dtos import ArticleDto, IgnoredDomainDto, TargetUrlDto, UrlDto
import numpy as np

class UrlRepositoryImpl(UrlRepository):
    def create(self, url: Url) -> None:
        url_dto = UrlDto.from_entity(url)
        url_dto.save()    
    
    def get_all(self) -> Url:
        dtos = UrlDto.select().execute()
        return self.__convert_to_entity(dtos)

    def get_by_id(self, id: int) -> Url:
        dtos = UrlDto.get_by_id(id)
        return self.__convert_to_entity(dtos)
    
    def get_by_url(self, url: str) -> Url:
        dtos =  UrlDto.select().where(UrlDto.url_str == url)
        return self.__convert_to_entity(dtos)

    def get_all_not_ignored(self) -> Url:
        dtos = UrlDto.select().where(UrlDto.ignored == False)
        return self.__convert_to_entity(dtos)

    def get_all_not_ignored_not_visited(self) -> Url:
        dtos = UrlDto.select().where((UrlDto.ignored == False) & (UrlDto.viewed == False))
        return self.__convert_to_entity(dtos)

    def __convert_to_entity(self, urls_dto) -> None:
        return UrlCollection([u.to_entity() for u in urls_dto])

    def update(self, url: Url) -> None:
        for url_entity in self.get_by_url(url.url):
            url_dto = UrlDto.from_entity(url_entity)
            url_dto.last_access = url.last_access
            url_dto.url_str = url.url_str
            url_dto.ignored = url.ignored
            url_dto.error = url.error
            url_dto.viewed = url.viewed
            url_dto.save()

    def delete_by_id(self, id: str) -> None:
        UrlDto.delete_by_id(id)

    def exists(self, url: Url) -> bool:
        urls = UrlDto.select().where(UrlDto.url_str == url.url_str)
        size = len(urls)
        return size > 0


class TargetsUrlRepositoryImpl(TargetUrlRepository):
    def create(self, url: TargetUrl):
        url_dto = TargetUrlDto.from_entity(url)
        url_dto.save()    

    def get_all(self):
        dto = TargetUrlDto.select()
        return self.__convert_to_entity(dto)

    def get_by_id(self, id: int) -> Url:
        dto = TargetUrlDto.get_by_id(id)
        return self.__convert_to_entity(dto)
    
    def get_by_url(self, url: str) -> Url:
        dto =  TargetUrlDto.select().where(TargetUrlDto.url_str == url)
        return self.__convert_to_entity(dto)

    def __convert_to_entity(self, dtos) -> None:
        return UrlCollection([d.to_entity() for d in dtos])

    def update(self, url: TargetUrl):
        for e in self.get_by_url(url.url):
            dto = TargetUrlDto.from_entity(e)
            dto.domain = url.domain.domain
            dto.url_str = url.url_str
            dto.save()

    def delete_by_id(self, id: str):
        raise NotImplementedError
    
    def exists(self, url: TargetUrl):
        target_dto = TargetUrlDto.from_entity(url)
        return len(TargetUrlDto.select().where(TargetUrlDto.url_str == target_dto.url_str)) > 0

class ArticlesRepositoryImpl(ArticlesRepository):
    
    def create(self, entity):
        dto = ArticleDto.from_entity(entity)
        dto.save()

    def get_all(self):
        dto = ArticleDto.select().execute()
        return self.convert_to_entity(dto)

    def get_by_id(self, id):
        dto = ArticleDto.get_by_id(id)
        return dto.to_entity()

    def update(self, entity):
        dto = ArticleDto.from_entity(entity)
        dto.save()
    
    def exists(self, url: Url):
        dto = ArticleDto.select().join(UrlDto).where(ArticleDto.url == url.id).execute()
        return len(dto) > 0
    
    def get_all_join_url(self):
        dto = ArticleDto.select().join(UrlDto).execute()
        return self.convert_to_entity(dto)

    def convert_to_entity(self, dtos) -> None:
        return [d.to_entity() for d in dtos]

class ArticlesRepositoryImplTester(ArticlesRepositoryImpl):

    def get_all(self):
        dto = ArticleDto.select().limit(10)
        return super().convert_to_entity(dto)

class IgnoredDomainRepositoryImpl(IgnoredDomainRepository):

    def create(self, entity):
        dto = IgnoredDomainDto.from_entity(entity)
        dto.save()

    def get_all(self):
        dto = IgnoredDomainDto.select().execute()
        return self.__convert_to_entity(dto)

    def get_by_id(self, id):
        dto = IgnoredDomainDto.get_by_id(id)
        return dto.to_entity()

    def update(self, entity):
        dto = IgnoredDomainDto.from_entity(entity)
        dto.save()

    def __convert_to_entity(self, dtos) -> None:
        return [d.to_entity() for d in dtos]