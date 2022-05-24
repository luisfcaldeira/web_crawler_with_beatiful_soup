import encodings
from bs4 import BeautifulSoup, NavigableString
import bs4
import requests
import collections.abc
import re


def getHTMLdocument(url):
    response = requests.get(url)
    return response.text
  
url_to_scrape = "https://www1.folha.uol.com.br/poder/2022/05/bolsonaro-dobra-numero-de-viagens-em-2022-e-acumula-eventos-com-perfil-eleitoral.shtml"
# url_to_scrape = "https://br.investing.com/news/stock-market-news/com-retomada-em-ny-ibovespa-sobe-171-e-recupera-o-nivel-de-110-mil-pontos-1002854"

html_document = getHTMLdocument(url_to_scrape)

html_test_document = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_document, 'lxml')
# soup = BeautifulSoup(html_document, 'html.parser')
tree = []


# kill all script and style elements
for script in soup(["script", "style"]):
    script.decompose()    # rip it out

# text = soup.get_text()
# f = open("teste_bs.txt", "w", encoding="UTF-8")
# f.write(text)
# f.close()

def seeker(elements):

    for element in elements:
        if element.name == 'div' \
            or element.name == 'header' \
            or element.name == 'article' \
            or element.name == 'main':
            if element.name == 'article':
                for article_elements in element.children:
                    if article_elements.name != None and article_elements.has_attr('class'):
                        print(article_elements.attrs['class'])

            seeker(element.children)
        else:    
            text_result = insert_into_tree(element)
            if text_result != None:
                tree.append(text_result.replace('\n', ''))


def insert_into_tree(element):
    
    if isinstance(element, bs4.element.Tag) and element.has_attr('class'):
        print(element.attrs['class']) 

    if element.name == 'article':
        print(element.name)
    if element.text == 'h1':
        print('h1')
        return element.text
        # return re.sub('[^A-Za-z0-9\s]+', '', element.text)


# seeker(soup.body)

# for sheet in tree:
#     print(sheet, '\n')

for h1 in soup.find_all('h1'):
    print(h1.text.encode('iso-8859-1').decode("UTF-8").strip())

for h2 in soup.find_all('h2'):
    print(h2.text.encode('iso-8859-1').decode("UTF-8").strip())

for dv in soup.find_all('div', {'class' : 'c-news__body'}):
    for p in dv.find_all('p'):
        paragraph = p.text.encode('iso-8859-1').decode("UTF-8")
        print(paragraph.strip())

for t in soup.find_all('time', {'class' : 'c-more-options__published-date'}):
    print(t.text.encode('iso-8859-1').decode("UTF-8").strip())
    

for p in dv.find_all('p', ):
    paragraph = p.text.encode('iso-8859-1').decode("UTF-8")
    print(paragraph.strip())