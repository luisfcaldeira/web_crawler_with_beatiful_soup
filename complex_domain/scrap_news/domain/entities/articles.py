
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
        return self.__decode_or_default(self.__title)

    @property
    def date(self):
        return self.__date

    @property
    def section(self):
        return self.__decode_or_default(self.__section)

    def __decode_or_default(self, txt):
        txt_result = ''
        if self.__section != None:
            try:
                txt_result = txt.encode('iso-8859-1').decode("UTF-8")
            except Exception:
                txt_result = txt
        return txt_result

    @property
    def text(self):
        return self.__decode_or_default(self.__text)
        
    @property
    def url(self):
        return self.__url

    def to_dict(self):
        if self.text == None:
            raise Exception("vazio")
        return { 'title' : self.title, 'date' : str(self.date), 'section' : self.section, 'url' : self.url.url_str, 'text' : self.text}