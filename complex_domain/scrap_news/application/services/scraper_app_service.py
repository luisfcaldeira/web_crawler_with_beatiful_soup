import datetime
from complex_domain.scrap_news.domain.entities.articles import Article
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import ArticlesRepositoryImpl, TargetsUrlRepositoryImpl, UrlRepositoryImpl
from complex_domain.scrap_news.infra.services.web_document import WebDocument
from complex_domain.scrap_news.services.web_crawler.folha_crawler_service import FolhaCrawlerService


class ScrapAppService():

    def __init__(self) -> None:
        self.__url_repository = UrlRepositoryImpl()
        self.__targets_repository = TargetsUrlRepositoryImpl()

    def run(self):
        targets = self.__convert_targets_into_urls()

        urls = self.__url_repository.get_all_not_ignored_not_visited()
        must_run = urls != None
        
        while must_run:

            for url in urls:
                self.__run_url(targets, url) 
                self.__url_repository.update(url=url)
                
            urls = self.__url_repository.get_all_not_ignored_not_visited()
            must_run = urls != None


    def __convert_targets_into_urls(self):
        targets = self.__targets_repository.get_all()
        urls = []
        for target in targets:
            target_url = Url(target.url_str)
            
            if not self.__url_repository.exists(target_url):
                self.__url_repository.create(url=target_url)

            urls.append(self.__url_repository.get_by_url(target.url_str)[0])

        return urls

    def __run_url(self, targets, url):
        print(f"accessing {url.url_str}")

        try:

            document = WebDocument(url.url_str)
            folha_crawler = FolhaCrawlerService(document)
            article_repository = ArticlesRepositoryImpl()

            url.last_access = datetime.datetime.now()

            anchors = folha_crawler.get_all_anchors_address()
            self.__collect_anchors(targets, anchors)  
            
            text = folha_crawler.get_news()
            date = folha_crawler.get_date()

            if date != None:
                date = datetime.datetime.strptime(date, r'%Y-%m-%d %H:%M:%S')

            title = folha_crawler.get_title()
            section = folha_crawler.get_section()

            article = Article(title=title, section=section, date=date, text=text, url=url)
            if article.is_valid():

                self.__save_article(url, article_repository, article)

        except Exception as e:
            print (e)
            url.ignored = True
            url.error = e
        
        

    def __save_article(self, url, article_repository, article):
        print('saving...')
        if article_repository.exists(url):
            article_repository.update(article)
        else:
            article_repository.create(article)

    def __collect_anchors(self, targets, anchors):
        for anchor in anchors:
            new_url = Url(anchor)

            new_url.ignored = not self.__contains_some_domain(targets, new_url)
            
            if not self.__url_repository.exists(new_url):
                self.__url_repository.create(url=new_url)
            else:
                self.__url_repository.update(url=new_url)

    def __contains_some_domain(self, targets, new_url):
        for target in targets:
            if new_url.contains(target.domain):
                return True
        return False
                
