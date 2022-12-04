from complex_domain.scrap_news.infra.services.web_document import Document, WebDocument
from complex_domain.scrap_news.services.web_crawler.beautiful_soup import BSCrawlerService



class MockWebDocument(Document):   

    def __init__(self, url: str) -> None:
        super().__init__('mock.web.document')

        self.__url = '''
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1>Title of test</h1>
                    <p>Paragraph of test
                        <a href='http://www.test.com'>Test</a>
                    </p>
                </body>
            </html>
        '''

        if url != None:
            self.__url = url

    def get_document(self) -> str:
        return self.__url

        

def test_find_anchors():
    bs_crawler = BSCrawlerService(MockWebDocument(
        '''
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1>Title of test</h1>
                    <p>Paragraph of test
                        <a href='http://www.test.com'>Test</a>
                        <a href='https://www.test2.com'>Test 2</a>
                        <a href='https://www.test3.com'>Test 3</a>
                    </p>
                </body>
            </html>
        '''
        )
    )

    gen_anchors = bs_crawler.get_all_anchors_address()

    assert gen_anchors != None
    
    anchors_test = [
        'http://www.test.com'
        , 'https://www.test2.com'
        , 'https://www.test3.com'
    ]

    anchors = list(gen_anchors)
    assert len(anchors) == len(anchors_test)

    for i in range(0, len(anchors)):
        assert anchors_test[i] == anchors[i]

def test_with_real_url():
    document = WebDocument("https://www1.folha.uol.com.br/mercado/2016/12/1838660-apos-dois-cortes-petrobras-eleva-precos-da-gasolina-e-do-diesel.shtml")
    bs_crawler = BSCrawlerService(document)
    links = bs_crawler.get_all_anchors_address()
    for link in links:
        print(link)