# test the files

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
from acme_report import *


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        '''test the stealability method for default'''
        prod = Product(name='TestSteal', price=10, weight=20)
        self.assertEqual(prod.stealability(), print('Kinda stealable'))

    def test_explode(self):
        '''test the explode method for new product'''
        prod = Product(name='flame-on', weight=30, flammability=4)
        self.assertEqual(prod.explode(), print('BABOOM!!'))


class AcmeReportTests(unittest.TestCase):
    '''checks that there is a list length of 30 for inventory report'''

    def test_default_num_products(self):
        '''test the lenth of the products list is 30'''
        prod_list = generate_products(num_products=30)
        self.assertEqual(len(prod_list), 30)


    def test_legal_names(self):
        '''Checks that the generated names for a
        default batch of products are all valid possible names to generate'''
        prod_list = generate_products()
        for product in prod_list:
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
