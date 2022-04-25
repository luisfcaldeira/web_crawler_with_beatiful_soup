from infra.services.web_document import MockWebDocument
from services.web_crawler.beautiful_soup import BSCrawler


def test_find_anchors():
    bs_crawler = BSCrawler(MockWebDocument('''
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
        '''))

    gen_anchors = bs_crawler.find_all_anchors()

    assert gen_anchors != None
    anchors_test = [
        'http://www.test.com'
        , 'http://www.test2.com'
        , 'http://www.test3.com'
    ]
    anchors = list(gen_anchors)
    assert len(anchors) == len(anchors_test)

    for i in range(0, len(anchors)):
        assert anchors_test[i] == anchors[i]