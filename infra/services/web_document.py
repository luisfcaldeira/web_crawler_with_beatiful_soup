import requests

from abc import ABC, abstractmethod


class Document(ABC):

    @property
    def url(self):
        return self.__url

    def __init__(self, url : str) -> None:
        super().__init__()
        self.__url = url
        
    @abstractmethod
    def get_document(self) -> str:
        pass


class WebDocument(Document):
    
    def get_document(self) -> str:
        response = requests.get(super().url)
        return response.text

class MockWebDocument(Document):

    def get_document(self) -> str:
        
        return '''
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1>Title of test</h1>
                    <p>Paragraph of test
                        <a href='http://www.test.com'>Test</a>
                        <a href='http://www.test2.com'>Test 2</a>
                        <a href='http://www.test3.com'>Test 3</a>
                    </p>
                </body>
            </html>
        '''