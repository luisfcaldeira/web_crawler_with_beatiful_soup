import pytest
from domain.entities.urls import Url
from domain.exceptions.urls_exceptions import MalFormedUrlException

def test_criacao_url():
    with pytest.raises(MalFormedUrlException):
        Url("http: // urlmalformada .c om")

def test_url_protocol():
    url = Url("https://www.domain.com")
    url2 = Url("www.domain.com")
    assert url.protocol.protocol == 'https' and url2.protocol.protocol == 'http'
    
def test_url_domain():
    url = Url("https://www.domain.com")
    print(url.domain.domain)
    url2 = Url("www.domain.com")
    assert url.domain.domain == 'www.domain.com' # and url2.domain.domain == 'www.domain.com'