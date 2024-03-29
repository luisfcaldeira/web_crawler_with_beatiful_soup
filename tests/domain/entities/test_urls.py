import re
from complex_domain.scrap_news.domain.entities.urls import Url, UrlCollection, TargetUrl

def test_criacao_url_com_erro():
    url = Url("I'm not an URL. ")
    
    assert url.valid == False


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
    url = Url("https://www1.domain1.com")
    url1 = Url("https://www1.domain1.com")
    url2 = Url("http://www1.domain1.com")
    url3 = Url("http://br.domain1.com")

    targets = [Url("http://www.folha.uol.com.br"), Url("https://www.folha.uol.com.br"), Url("http://www1.folha.uol.com.br")]
    folha2 = Url("https://www.folha.uol.com.br")
    folha3 = Url("https://top-of-mind.folha.uol.com.br/2021/")
    folha4 = Url("http://transparencia.folha.uol.com.br ")

    assert url == url1
    assert url1 != url2
    assert url1 != url3
    assert folha2 in targets
    assert folha3 not in targets
    assert folha4 not in targets

def test_if_a_domain_is_contained_in_a_url():
    url1 = Url("https://www.domain1.com")
    domain = url1.domain

    url2 = Url("https://subdomain.domain1.com")
    url3 = Url("https://subdomain.domain2.com")

    assert url1.contains(domain) == True
    assert url2.contains(domain) == True
    assert url3.contains(domain) == False

def test_url_collection():
    url1 = Url("http://www.domain.com")
    url2 = Url("http://www.domain1.com")
    url_collection1 = UrlCollection([url1, url2])
    url_collection2 = UrlCollection([url1])

    url = url_collection2.exclude(url_collection1)[0]

    assert url == url2

def test_real_url():
    url1 = Url("https://www1.folha.uol.com.br/credibilidade/folha-no-projeto-credibilidade.shtml")

    assert url1.ignored == False
    assert url1.contains(domain=TargetUrl('folha.uol.com.br').domain) == True

def test_apply_rules():
    url_str = "https://www1.folha.uol.com.br/livrariadafolha/2016/10/1580436-receitas-para-dormir-bem-sugere-como-ter-uma-noite-tranquila.shtml"
    url1 = Url(url_str)
    pattern = r'.+\/2016\/\d{2}[\/0-9\-a-z]+\.shtml$'
    assert re.match(pattern, url_str) != None
    assert url1.is_accepted({'pattern': pattern})

