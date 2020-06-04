import requests
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(filename='scrapping.log',level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(name)s %(message)s')


def buco(sku):
    import sys
    logging.info('funtion : buco')

    urlll = 'https://www.buco.co.za/default/catalogsearch/result/?q={0}'.format(sku)
    data = requests.get(urlll)
    soup = BeautifulSoup(data.text, 'html.parser')
    try:
        links = []
        for a in soup.find_all('a', {'class': 'product-item-link'}):  # can use 'class':'product photo product-item-photo' also
            links.append(a['href'])
        for link in links:
            if str(sku) in link:
                product_link = link
            else:
                product_link = None
        # if product link is empty raise error as product link not found or verify sku
        if product_link is None:
            raise Exception
    except Exception:
        # price = ""
        logging.error('Verify Sku ,product link not found ')

    else:
        try:
            data = requests.get(product_link)
            soup = BeautifulSoup(data.text, 'html.parser')
            skudetails = soup.find('form', {'data-product-sku': str(sku)})
            product_id = skudetails.find('input', {'name': 'product'})['value']
            price = soup.find('span', {'id': 'product-price-' + product_id})['data-price-amount']
            logging.info(msg=f'sku= {sku} ,product_id = {product_id}, price = {price}')
            return price

        except KeyError as k:
            # price = ''
            logging.error(msg=f'cannot fetch product_id or price,  error key = {k}')
            #logging.info(sys.exc_info())

        except Exception :
            # price = ''
            logging.exception('unknown error')

        # finally:
        #     if price = "":
        #         #get previous price of sku from database
        #
        #     else:
        #         return price


def builders(sku):
    logging.info('function : builders')

    urlll = 'https://www.builders.co.za/search/?text={0}'.format(int(sku))
    data = requests.get(urlll)
    soup = BeautifulSoup(data.text, 'html.parser')
    try:
        x = soup.find('a', {'id': "productLink000000000000" + str(sku)})
        if x is None:
            raise Exception
    except Exception:
        logging.error(msg='Sku is invalid')

    else:
        price = x['data-product-price']
        if price == "":
            logging.error(msg='Product is not available --> data-productavailable="false" ') #product is not available anymore
        return price


def leroy(sku):
    logging.info('funtion = leroy')

    urlll = 'https://leroymerlin.co.za/catalogsearch/result/?q={0}'.format(sku)
    data = requests.get(urlll)
    soup = BeautifulSoup(data.text, 'html.parser')
    try:
        form = soup.find('form', {'data-product-sku' : str(sku)})
        product_id = form.find('input', {'name':'product'})['value']
        price = soup.find('span', {'id':"price-including-tax-product-price-"+product_id})['data-price-amount']
        return  price

    except AttributeError:
        # price = ''
        logging.error('Sku is invalid')
    except KeyError as k:
        # price = ''
        logging.error(msg=f'cannot fetch product_id or price,  error key = {k}')
    except Exception:
        # price = ''
        logging.exception('unknown error..!')

    # finally:
    #     if price = "":
    #         #get previous price of sku from database
    #     else:
    #         return price


def cashbuild(sku):
    logging.info('function : cashbuild')

    cashbuild_url = 'https://www.cashbuildonline.co.za/search?q={0}'.format(sku)
    data = requests.get(cashbuild_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    try:
        product_details = soup.find_all('div', {'class': 'product_name'})
        if len(product_details) == 1:
            product_link_extn = product_details[0].find('a')['href']
        else:
            raise Exception
    except Exception:
        logging.error('Invalid Sku, getting None or more than one product')

    else:
        product_url = 'https://www.cashbuildonline.co.za' + product_link_extn
        data = requests.get(product_url)
        soup = BeautifulSoup(data.text, 'html.parser')
        text_ = soup.find('select', {'id': 'product-select'}).text
        price = re.sub('[^0-9.]*', "", text_)

        return price


# def check():
#     builders_sku = [627935, 627940, 627933, 639106, 517797, 634913, 627953, 655546]
#     leroy_sku = [ 81424182, 81412024, 81422547, 81412025, 81422548, 81437685, 81437684 ]
#     buco_sku = [ 1203434, 1161188, 1016533, 1313309, 1255586,1231008, 1179899, 1291750 , 1035145]
#     cashbuild_sku = [ 303275,305661]
#
#     for sku in cashbuild_sku:
#         print('cashbuild : ', sku, cashbuild(sku))
#         break
#
#     for sku in builders_sku:
#         print('builders_sku : ',sku, builders(sku))
#         break
#
#     for sku in leroy_sku:
#         print("leroy_sku : ",sku, leroy(sku))
#         break
#
#     for sku in buco_sku:
#         print('buco_sku : ',sku, buco(sku))
#         break
#
# check()