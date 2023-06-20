import requests
from lxml import etree
from bs4 import BeautifulSoup

class DataDom:
    def __init__(self, watchlist, HEADER, CURRENCY_SYMBOL):
        self.watchlist = watchlist
        self.HEADER = HEADER
        self.CURRENCY_SYMBOL = CURRENCY_SYMBOL

    def get_current_price(self, dom):
        try:
            product_current_price = dom.xpath('//span[@class="a-offscreen"]/text()')[0]
            return float(product_current_price.replace(self.CURRENCY_SYMBOL, ''))
        except Exception as e:
            return e
    
    def get_listed_name(self, dom):
        try:
            product_name = dom.xpath('//span[@id="productTitle"]/text()')       
            return str(product_name[0].strip())
        except Exception as e:
            return e
        
    def get_rrp(self, dom):
        try:
            product_rrp = dom.xpath('//span[@class="a-offscreen"]/text()')[5]
            return float(product_rrp.replace(self.CURRENCY_SYMBOL, ''))
        except Exception as e:
            return e
    
    def calculate_discount(self, current_price, rrp):
        return round(1 - (current_price / rrp), 2)
        
    def get_all_products(self):
        all_products = []

        for url in self.watchlist:
            url_link = self.watchlist[url]
            response = requests.get(url_link, headers=self.HEADER)
            raw_html = BeautifulSoup(response.content, 'html.parser')
            html_dom = etree.HTML(str(raw_html))

            product_name = self.get_listed_name(html_dom)
            product_current_price = self.get_current_price(html_dom)
            product_rrp = self.get_rrp(html_dom)
            product_discount = self.calculate_discount(product_current_price, product_rrp)

            print(f"Adding product -> {product_name}")

            all_products.append([url_link, product_name, product_rrp, product_current_price, product_discount])
        
        return all_products