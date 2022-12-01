
from complex_domain.scrap_news.services.web_crawler.beautiful_soup import BSCrawlerService


class FolhaCrawlerService(BSCrawlerService):

    def get_title(self):
        return super().get_title()

    def get_date(self):
        return super().get_meta('article:published_time')

    def get_section(self):
        section = super().get_meta('article:section')
        if section == None or section == '':
            divs = self.find_all_div("section-masthead")
            if len(divs) > 0:
                return super().find_a(wrapper_element=divs[0])[0].text

    def get_news(self):
        text = self.get_content_by_class()
        if text == None:
            text = self.get_content_by_property_itemprop()
        
        return text

    def get_content_by_property_itemprop(self):
        divs = self.get_div_by_property('itemprop', 'articleBody')
        if len(divs) > 0:
            return super().get_all_p_content(wrapper_element=divs[0])
        return None

    def get_content_by_class(self):
        clazz = 'c-news__body'
        text = None
        divs = super().find_all_div(class_name=clazz)
        if len(divs) > 0:
            text = super().get_all_p_content(wrapper_element=divs[0])
        return text

