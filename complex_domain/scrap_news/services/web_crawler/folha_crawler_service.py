
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.services.web_document import WebDocument
from complex_domain.scrap_news.services.web_crawler.beautiful_soup import BSCrawlerService


class FolhaCrawlerService(BSCrawlerService):

    def get_title(self):
        return super().get_title()

    def get_date(self):
        return super().get_meta('article:published_time')

    def get_section(self):
        return super().get_meta('article:section')

    def get_news(self):

        divs = super().find_all_div(class_name='c-news__body')
        text = None
        
        if len(divs) > 0:
            text = super().get_all_p_content(wrapper_element=divs[0])
        return text