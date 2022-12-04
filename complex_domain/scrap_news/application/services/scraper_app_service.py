from asyncio.log import logger
import datetime
from complex_domain.scrap_news.domain.dal.repositories.entities_repositories import IgnoredDomainRepository, TargetUrlRepository, UrlRepository
from complex_domain.scrap_news.domain.entities.articles import Article
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import ArticlesRepositoryImpl
from complex_domain.scrap_news.infra.services.terminal_services import ConsoleLogger, ErrorLoggerProfile, InfoLoggerProfile, WarningLoggerProfile
from complex_domain.scrap_news.infra.services.web_document import WebDocument
from complex_domain.scrap_news.services.web_crawler.folha_crawler_service import FolhaCrawlerService
import numpy as np


    
class ScrapAppService():

    def __init__(self, url_repository: UrlRepository, targets_repository: TargetUrlRepository, console_logger: ConsoleLogger, ignored_domain_repository: IgnoredDomainRepository) -> None:

        if not isinstance(url_repository, UrlRepository) or not isinstance(targets_repository, TargetUrlRepository) or not isinstance(console_logger, ConsoleLogger) or not isinstance(ignored_domain_repository, IgnoredDomainRepository):
            raise Exception('Make sure you are passing right types for ScrappAppService\'s constructor.')

        self.__url_repository = url_repository
        self.__targets_repository = targets_repository
        self.__ignored_domain_repository = ignored_domain_repository
        self.__logger = console_logger
        self.__targets = self.__targets_repository.get_all()
        self.__counter_of_saved_articles = 0
        self.__counter_of_accessed_url = 0
        self.__urls = []

    def run(self, rule, save_only_referred_anchors=True, include_target_in_list=False):

        if include_target_in_list:
            self.__convert_targets_into_urls()

        while True:
            
            self.__logger.log_this('=> getting all non visited sites...')
            self.__urls = self.__url_repository.get_all_not_ignored_not_visited()
            self.__logger.log_this(f'=> it was found {len(self.__urls)} records', profile=InfoLoggerProfile())

            if len(self.__urls) == 0:
                return

            for url in self.__urls:
                self.__logger.log_this('=> next url...')
                self.__logger.log_this(url.url_str)
                
                if not url.ignored and url.domain not in self.__ignored_domain_repository.get_all():
                    url.last_access = datetime.datetime.now()

                    if url.is_accepted(rule):
                        self.__run_url(url, save_only_referred_anchors) 
                        self.__counter_of_accessed_url += 1
                    else:
                        url.ignored = True
                        url.error = 'Url isn\'t accepted by rules'
                        self.__logger.log_this('Not accepted by rules', profile=WarningLoggerProfile())

                    self.__url_repository.update(url=url)
                    self.__logger.log_this(f'=> it was accessed {self.__counter_of_accessed_url} urls and was saved {self.__counter_of_saved_articles} articles...', profile=InfoLoggerProfile())

    def __convert_targets_into_urls(self):
        targets = self.__targets_repository.get_all()
        total = len(targets)
        self.__logger.log_this(f'converting {len(targets)} targets... wait')
        counter = 0
        for target in targets:
            counter += 1
            target_url = Url(target.url_str)
            
            if not self.__url_repository.exists(target_url):
                self.__logger.log_this(f'saving #{counter}/{total} {target_url}')
                self.__url_repository.create(url=target_url)

    def __run_url(self, url, save_only_referred_anchors=True):
        self.__logger.log_this(f"=> accessing")

        try:
            folha_crawler = self.__read_document(url)
            self.__logger.log_this('=> document\'s ready.. saving anchors')
            anchors = folha_crawler.get_all_anchors_address()
            article = self.__construct_and_sabe_article(url, folha_crawler)

            if article.is_valid() or save_only_referred_anchors:
                self.__save_anchors(anchors)  

        except Exception as e:
            self.__logger.log_this(e, profile=ErrorLoggerProfile())
            url.ignored = True
            url.error = str(e)


    def __read_document(self, url):
        self.__logger.log_this('=> opening site...')
        document = WebDocument(url.url)
        self.__logger.log_this('=> scraping all site...')
        folha_crawler = FolhaCrawlerService(document)
        return folha_crawler

    def __construct_and_sabe_article(self, url, folha_crawler):
        self.__logger.log_this('=> constructing article')

        text = folha_crawler.get_news()
        date = folha_crawler.get_date()
        title = folha_crawler.get_title()
        section = folha_crawler.get_section()

        if date != None:
            date = datetime.datetime.strptime(date, r'%Y-%m-%d %H:%M:%S')

        article = Article(title=title, section=section, date=date, text=text, url=url)

        if article.is_valid():
            self.__logger.log_this(f"=> title '{article.title}'")
            self.__logger.log_this(f"=> date of publish [{article.date}]")
            self.__logger.log_this(f"=> saving...")

            self.__save_article(url, article)

            self.__counter_of_saved_articles += 1
        else:
            self.__logger.log_this(f"=> no article was found, ignoring...")
        
        return article
    
    def __save_article(self, url, article):
        article_repository = ArticlesRepositoryImpl()
        if article_repository.exists(url):
            article_repository.update(article)
        else:
            article_repository.create(article)

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
                self.__logger.log_this('error on trying to save URL:', e, profile=ErrorLoggerProfile())

    def __it_should_to_be_saved(self, new_url: Url):
        if not new_url.valid:
            return False

        for target in self.__targets:
            if new_url.contains(target.domain):
                return True
        return False
                
