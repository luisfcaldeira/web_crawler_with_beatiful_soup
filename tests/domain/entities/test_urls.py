import pytest
from complex_domain.scrap_news.domain.entities.urls import Url
from complex_domain.scrap_news.domain.exceptions.urls_exceptions import MalFormedUrlException

def test_criacao_url_com_erro():
    with pytest.raises(MalFormedUrlException):
        Url("http: // urlmalformada .c om")
    
    with pytest.raises(MalFormedUrlException):
        Url("I'm not an URL. ")

    with pytest.raises(MalFormedUrlException):
        Url("fakeurl. com")

def test_url_protocol():
    url = Url("https://www.domain.com")
    assert url.protocol.protocol == 'https' 

def test_default_protocol():
    url = Url("www.noprotocol.com")
    assert url.protocol.protocol == 'http'
    
def test_url_domain():
    url = Url("https://www.domain.com")
    url2 = Url("www.domain.com")
    assert url.domain.domain == 'domain.com' 
    assert url2.domain.domain == 'domain.com'

def test_equals_url():
    url1 = Url("https://www1.domain1.com")
    url2 = Url("http://www1.domain1.com")

    assert url1 == url2