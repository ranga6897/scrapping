import requests
from bs4 import BeautifulSoup
import re



def builders(sku):
    urlll = 'https://www.builders.co.za/search/?text={0}'.format(int(sku))
    data = requests.get(urlll)

    soup = BeautifulSoup(data.text, 'html.parser')
    x = soup.find('a', {'class': 'description producturl track-product-click'})
    if x is not None:
        price = x.attrs['data-product-price']
    else:
        price = 'not found'

    return price


def leroy(sku):
    urlll = 'https://leroymerlin.co.za/catalogsearch/result/?q={0}'.format(sku)
    data = requests.get(urlll)

    soup = BeautifulSoup(data.text, 'html.parser')
    span = soup.find('span', {'class': 'price'})
    if span is not None:
        price = re.sub('[a-z]*','',span.text, flags=re.IGNORECASE)
    else:
        price = 'not found'

    return price


def buco(sku):
    urlll = 'https://www.buco.co.za/default/catalogsearch/result/?q={0}'.format(sku)
    data = requests.get(urlll)

    soup = BeautifulSoup(data.text, 'html.parser')
    span = soup.find('span', {'class': 'price'})
    if span is not None:
        price = re.sub('[a-z]*','',span.text, flags=re.IGNORECASE)
    else:
        price = 'not found'

    return price


def cashbuild(sku):
    cashbuild_url = 'https://www.cashbuildonline.co.za/search?q={0}'.format(sku)
    data = requests.get(cashbuild_url)

    soup = BeautifulSoup(data.text, 'html.parser')
    x = soup.find('div', {'class': 'product_name'})
    links_with_text = [a['href'] for a in x.find_all('a', href=True) if a.text]
    product_url = 'https://www.cashbuildonline.co.za' + links_with_text[0]

    data = requests.get(product_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    text_ = soup.find('select', {'id': 'product-select'}).text
    pattern = re.compile(r'[0-9./]*')
    price = list(filter(None, pattern.findall(text_)))[0]
    if price is not None:
        return price
