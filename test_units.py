import config
import filecmp
import unittest
from datadom import DataDom
from products import Products
from email_sender import EmailSender
import pandas.testing as pd_testing

global datadom
global product_sets
global products
global email_sender

"""
Fast Object class, Function, and File testing
"""
class TestDataDom(unittest.TestCase):
    
    def test_initDataDom(self):
        self.assertIsInstance(datadom, DataDom)
    
    def test_getProducts(self):
        self.assertIsInstance(product_sets, list)

class TestProducts(unittest.TestCase):
    
    def test_initProducts(self):
        self.assertIsInstance(products, Products)
    
    def test_writeToCSV(self):
        products.write_to_csv(product_sets, './test-units/test_products.csv')
        self.assertTrue(filecmp.cmp('./test-units/test_products.csv', './test-units/test_products.csv'))

    def test_csvDiscountAnalysis(self):
        output = products.csv_discount_analysis('./test-units/test_products.csv', config.discount_boundary)
        pd_testing.assert_frame_equal(output, output)

    def test_writeToJson(self):
        output = products.write_to_json(product_sets, './test-units/test_products.json')
        self.assertTrue(filecmp.cmp('./test-units/test_products.json', './test-units/test_products.json'))
        

class TestEmailSender(unittest.TestCase):
    
    def test_initEmailSender(self):
        self.assertIsInstance(email_sender, EmailSender)
    
if __name__ == '__main__':
    datadom = DataDom(config.watchlist, config.HEADER, config.CURRENCY_SYMBOL)
    product_sets = datadom.get_all_products()
    products = Products()
    email_sender = EmailSender(config.EMAIL_ADDRESS, config.CURRENCY_SYMBOL)
    unittest.main()