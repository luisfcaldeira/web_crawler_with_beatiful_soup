
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
        return self.__title

    @property
    def date(self):
        return self.__date

    @property
    def section(self):
        return self.__section

    @property
    def text(self):
        return self.__text
        
    @property
    def url(self):
        return self.__url