from itertools import product
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def scrape_html(base_url, page):

    base_url = base_url
    page = page

    url = base_url + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    return soup

def get_page_content(soup):

    soup = soup
    products_info_content = soup.find_all('div',class_='product-card__content')
    return products_info_content

def get_page_price(soup):
    soup = soup
    products_info_price = soup.find_all('div', class_='product-card__price')
    return products_info_price

def get_product_name(products_info_content):
    products_info_content=products_info_content

    products_name = []

    for product in range(len(products_info_content)):
        name_p = products_info_content[product].find_all('p')[0]
        alcohol_name = name_p.contents[0].strip()

        products_name.append(alcohol_name)
    
    converter = lambda x: x.replace(' ', '_')
    products_name = list(map(converter, products_name))

    return products_name

def get_product_alcohol_percent(products_info_name):
    products_info_name = products_info_name
    products_percent = []

    for product in range(len(products_info_content)):

        name_per = products_info_content[product].find_all('p')[1]
        print(name_per)
        alcohol_percent_str = name_per.contents[0].strip()
        print(alcohol_percent_str)
        start = alcohol_percent_str.find('/')
        end = alcohol_percent_str.find('%')

        alcohol_percent = alcohol_percent_str[start + 2: end]

        
        products_percent.append(alcohol_percent)

    return products_percent

scrape = scrape_html(base_url ="https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg=" , page=1)

products_info_content =get_page_content(scrape)
products_name = get_product_name(products_info_content)
products_percent = get_product_alcohol_percent(products_info_content)



#print(products_name)
print(products_percent)