



from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import ArticlesRepositoryImplTester, UrlRepositoryImpl


def test_data():
    repo = ArticlesRepositoryImplTester()
    articles = repo.get_all()
    len(articles) == 10

def test_if_url_exists():
    repo = UrlRepositoryImpl()
    assert repo.exists(Url("http://www1.folha.uol.com.br/mercado/2016/10/1820053-brasil-so-atingira-superavit-primario-em-2020-afirma-fmi.shtml"))

    