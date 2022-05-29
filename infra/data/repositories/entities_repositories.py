


from domain.dal.repositories.entities_repositories import UrlRepository
from domain.entities.urls import Url
from infra.data.dtos.dtos import UrlDto


class UrlRepositoryImpl(UrlRepository):
    def create(self, url: Url):
        url_dto = UrlDto.from_entity(url)
        url_dto.save()    

    def find_by_id(self, id: str) -> Url:
        raise NotImplementedError

    def update(self, url: Url):
        raise NotImplementedError

    def delete_by_id(self, id: str):
        raise NotImplementedError