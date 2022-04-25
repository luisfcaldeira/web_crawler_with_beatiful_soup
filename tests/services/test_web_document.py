from infra.services.web_document import MockWebDocument
from services.web_crawler.beautiful_soup import BSCrawler


def test_find_anchors():
    bs_crawler = BSCrawler(MockWebDocument(''))

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