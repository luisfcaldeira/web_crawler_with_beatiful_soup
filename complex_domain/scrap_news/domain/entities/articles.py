
class Article():

    def __init__(self, title, date, section, text, url, id = None) -> None:
        self.__id = id
        self.__title = title
        self.__date = date
        self.__section = section
        self.__text = text
        self.__url = url

    def is_valid(self):
        return self.__text != None and self.__text != ""

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        title = ''
        if self.__title != None:
            try:
                title = self.__title.encode('iso-8859-1').decode("UTF-8")
            except Exception:
                title = self.__title

        return title

    @property
    def date(self):
        return self.__date

    @property
    def section(self):
        section = ''
        if self.__section != None:
            try:
                section = self.__section.encode('iso-8859-1').decode("UTF-8")
            except Exception:
                section = self.__section

        return section

    @property
    def text(self):
        return self.__text
        
    @property
    def url(self):
        return self.__url

    def to_dict(self):
        return { 'title' : self.title, 'date' : self.date, 'section' : self.section, 'url' : self.url.url_str, 'text' : self.text}