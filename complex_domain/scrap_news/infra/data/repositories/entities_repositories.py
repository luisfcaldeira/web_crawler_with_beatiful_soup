from complex_domain.scrap_news.domain.dal.repositories.entities_repositories import TargetUrlRepository, UrlRepository
from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url
from complex_domain.scrap_news.infra.data.dtos.dtos import TargetUrlDto, UrlDto


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

    def __convert_to_entity(self, urls_dto) -> None:
        return [u.to_entity() for u in urls_dto]

    def update(self, url: Url) -> None:
        for url_entity in self.get_by_url(url.url):
            url_dto = UrlDto.from_entity(url_entity)
            url_dto.last_access = url.last_access
            url_dto.url_str = url.url_str
            url_dto.ignored = url.ignored
            url_dto.save()

    def delete_by_id(self, id: str) -> None:
        UrlDto.delete_by_id(id)

    def exists(self, url: Url) -> None:
        return len(UrlDto.select().where(UrlDto.url_str == url.url_str)) > 0


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
        return [d.to_entity() for d in dtos]

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

