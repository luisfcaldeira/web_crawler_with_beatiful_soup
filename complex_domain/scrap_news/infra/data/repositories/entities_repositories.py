


from complex_domain.scrap_news.domain.dal.repositories.entities_repositories import TargetUrlRepository, UrlRepository
from complex_domain.scrap_news.domain.entities.urls import TargetUrl, Url
from complex_domain.scrap_news.infra.data.dtos.dtos import TargetUrlDto, UrlDto


class UrlRepositoryImpl(UrlRepository):
    def create(self, url: Url):
        url_dto = UrlDto.from_entity(url)
        url_dto.save()    
    
    def get_all(self):
        return UrlDto.select().execute()

    def get_by_id(self, id: int) -> Url:
        raise NotImplementedError
    
    def get_by_url(self, url: str) -> Url:
        return UrlDto.select().where(UrlDto.url_str == url)

    def update(self, url: Url):
        for url_dto in self.get_by_url(url.url):
            url_dto.last_access = url.last_access
            url_dto.url_str = url.url_str
            url_dto.ignored = url.ignored
            url_dto.save()

    def delete_by_id(self, id: str):
        raise NotImplementedError

    def exists(self, url: Url):
        return len(UrlDto.select().where(UrlDto.domain == url.domain.domain)) > 0


class TargetsUrlRepositoryImpl(TargetUrlRepository):
    def create(self, url: TargetUrl):
        url_dto = TargetUrlDto.from_entity(url)
        url_dto.save()    

    def get_all(self):
        return TargetUrlDto.select()

    def get_by_id(self, id: int) -> Url:
        raise NotImplementedError

    def update(self, url: Url):
        raise NotImplementedError

    def delete_by_id(self, id: str):
        raise NotImplementedError
    
    def exists(self, url: TargetUrl):
        target_dto = TargetUrlDto.from_entity(url)
        return len(TargetUrlDto.select().where(TargetUrlDto.domain == target_dto.domain)) > 0

