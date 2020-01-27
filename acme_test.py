import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Tests default product weight being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_name(self):
        """Test product name string returns appropriately"""
        prod = Product('Test Product')
        self.assertEqual(prod.name, 'Test Product')

    def test_product_stealability(self):
        """Test stealability computes properly"""
        prod = Product('Test Product')  # checks on default product
        self.assertTrue(prod.stealability() == 'Kinda stealable')
        prod = Product('Test Product 2', weight=100)  # checks on product with new weight
        self.assertTrue(prod.stealability() == 'Not so stealable...')
        prod.price = 500  # checks on product with new price, ensures all options for stealability work properly
        self.assertTrue(prod.stealability() == 'Very stealable!')

    def test_explode(self):
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeBoxingGloveTests(unittest.TestCase):
    def test_punch(self):
        glove = BoxingGlove('test')
        self.assertTrue(BoxingGlove.punch() == 'Hey that hurt!')
        glove.weight = 15
        self.assertTrue(BoxingGlove.punch() == 'OUCH!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Ensures product generator creates 30 products"""
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)

    def test_legal_names(self):
        """Checks generated names to ensure they are allowed"""
        prod_list = generate_products()
        for item in prod_list:
            adj = item.name.split()[0]
            noun = item.name.split()[1]
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)
            self.assertIn(' ', item.name)

    def test_report(self):
        """Tests that the report returns all the values it should"""
        avg_price, avg_weight, avg_flammability = inventory_report(generate_products())
        self.assertIsNotNone(avg_price)
        self.assertIsNotNone(avg_weight)
        self.assertIsNotNone(avg_flammability)


if __name__ == '__main__':
    unittest.main()
