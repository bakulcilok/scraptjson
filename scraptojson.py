import requests
from bs4 import BeautifulSoup as soup
import os
import json

URL = "URL PARA MAPEAR"
page = requests.get(URL)
page_html = soup(page.text, 'lxml')

product_elements = page_html.find_all("div", class_="ui-search-result__wrapper")

for pages in page_html:
    list_of_products = []
#scrapper
    for product_element in product_elements:
        link = product_element.find("a", class_="ui-search-link")
        link_element = link.get('href')
        title_element = product_element.find("h2", class_="ui-search-item__title")
        image = product_element.find("img", class_="ui-search-result-image__element")
        image_element = image.get('data-src')
        price_element = product_element.find("span", class_="price-tag-amount")

        list_of_products.append({
            'name_product': title_element.text.strip(),
            'image_product': image_element.strip(),
            'price_product': price_element.text.strip(),
            'link_product': link_element.strip(),
        })

with open("NOME_DO_ARQUIVO.json", "w") as outfile:
    for product in list_of_products:
        json.dump(list_of_products, outfile)
        outfile.write('\n')
