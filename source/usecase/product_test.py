import unittest
from product import ProductUseCase


class ProductUseCaseTest(unittest.TestCase):

    def test_get_product(self):
        product_usecase = ProductUseCase()

        products = product_usecase.get_products()
        self.assertEqual(len(products), 6)

    def test_get_products_with_discount_price(self):
        product_usecase = ProductUseCase()
        products = product_usecase.get_products_with_discount_price()
        self.assertEqual(len(products), 6)
        self.assertEqual(products[0].price, 0.45)