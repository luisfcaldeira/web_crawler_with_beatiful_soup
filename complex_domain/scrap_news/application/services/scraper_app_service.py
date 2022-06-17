import datetime
from complex_domain.scrap_news.domain.entities.articles import Article
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import ArticlesRepositoryImpl, TargetsUrlRepositoryImpl, UrlRepositoryImpl
from complex_domain.scrap_news.infra.services.web_document import WebDocument
from complex_domain.scrap_news.services.web_crawler.folha_crawler_service import FolhaCrawlerService
import numpy as np

class Logger():

    def __init__(self) -> None:
        self.__now = datetime.datetime.now()

    def log_this(self, msg=None):
        new_now = datetime.datetime.now()
        print(new_now - self.__now, end=' ')
        self.__now = new_now

        if msg != None:
            print(msg)

class ScrapAppService():

    def __init__(self) -> None:
        self.__url_repository = UrlRepositoryImpl()
        self.__targets_repository = TargetsUrlRepositoryImpl()
        self.__targets = self.__targets_repository.get_all()
        self.__time_calc = Logger()
        self.__urls = []

    def run(self):

        self.__convert_targets_into_urls()
        
        while True:
            self.__time_calc.log_this('=> getting all non visited sites...')
            self.__urls = self.__url_repository.get_all_not_ignored_not_visited()

            if len(self.__urls) == 0:
                return

            for url in self.__urls:
                self.__time_calc.log_this('=> next url...')
                
                url.last_access = datetime.datetime.now()
                self.__run_url(url) 
                self.__url_repository.update(url=url)
            
    def __convert_targets_into_urls(self):
        targets = self.__targets_repository.get_all()

        for target in targets:
            target_url = Url(target.url_str)
            
            if not self.__url_repository.exists(target_url):
                self.__url_repository.create(url=target_url)

    def __run_url(self, url):
        print(f"accessing [{url.url_str}]", end=' ')

        try:
            folha_crawler = self.__read_document(url)
            
            self.__time_calc.log_this('=> document\' is read.. saving anchors')

            anchors = folha_crawler.get_all_anchors_address()

            self.__save_anchors(anchors)  
            
            self.__construct_article(url, folha_crawler)

        except Exception as e:
            print (e)
            url.ignored = True
            url.error = e

    def __read_document(self, url):
        self.__time_calc.log_this('=> opening site...')
        document = WebDocument(url.url_str)
        folha_crawler = FolhaCrawlerService(document)
        return folha_crawler

    def __save_article(self, url, article):
        article_repository = ArticlesRepositoryImpl()

        print('saving...')
        if article_repository.exists(url):
            article_repository.update(article)
        else:
            article_repository.create(article)

    def __construct_article(self, url, folha_crawler):
        self.__time_calc.log_this('=> constructing article')
        text = folha_crawler.get_news()
        date = folha_crawler.get_date()

        if date != None:
            date = datetime.datetime.strptime(date, r'%Y-%m-%d %H:%M:%S')

        title = folha_crawler.get_title()
        section = folha_crawler.get_section()

        article = Article(title=title, section=section, date=date, text=text, url=url)

        if article.is_valid():
            self.__save_article(url, article)
        else:
            print("ignoring...")
    
    def __save_anchors(self, anchors):
        anchors = np.array([Url(anchor) for anchor in anchors])
        anchors = self.__urls.exclude(anchors)

        for anchor in anchors:
            try:
                anchor.ignored = not self.__it_should_to_be_saved(anchor)
                
                if not self.__url_repository.exists(anchor):
                    self.__url_repository.create(url=anchor)
                else:
                    self.__url_repository.update(url=anchor)

            except Exception as e:
                print('error on trying to save URL:', e)

    def __it_should_to_be_saved(self, new_url: Url):
        if not new_url.valid:
            return False

        for target in self.__targets:
            if new_url.contains(target.domain):
                return True
        return False
                
