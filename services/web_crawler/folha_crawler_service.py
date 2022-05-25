
from domain.entities.urls import Url
from infra.services.web_document import WebDocument
from services.web_crawler.beautiful_soup import BSCrawlerService


class FolhaCrawlerService(BSCrawlerService):

    def get_news(self):

        divs = super().find_all_div(class_name='c-news__body')

        text = super().get_all_p_content(wrapper_element=divs[0])

        return text