



from complex_domain.scrap_news.infra.data.repositories.entities_repositories import ArticlesRepositoryImplTester


def test_data():
    repo = ArticlesRepositoryImplTester()
    articles = repo.get_all()

    
    len(articles) == 10