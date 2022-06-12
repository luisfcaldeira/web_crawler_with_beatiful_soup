
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.infra.services.web_document import WebDocument
from complex_domain.scrap_news.services.web_crawler.beautiful_soup import BSCrawlerService


class FolhaCrawlerService(BSCrawlerService):

    def get_news(self):

        divs = super().find_all_div(class_name='c-news__body')

        text = super().get_all_p_content(wrapper_element=divs[0])

        return text