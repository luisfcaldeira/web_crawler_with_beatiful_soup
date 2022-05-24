from infra.services.web_document import MockWebDocument
from services.web_crawler.beautiful_soup import BSCrawlerService


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

    gen_anchors = bs_crawler.find_all_anchors()

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