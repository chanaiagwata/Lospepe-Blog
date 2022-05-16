import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that runs before every Test
        """
        self.random_quote = Quote("Johen Cena", "Winners don't quit")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author, "John Cena")
        self.assertEqual(self.random_quote.quote,"Winners don't quit")