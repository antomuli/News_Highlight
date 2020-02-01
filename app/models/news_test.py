import unittest
from models import news
News = news.News

class NewsTest(unitest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
      '''
      Set up method that will run before every test
      '''
      self.new_news = news(1234, 'Coronavirus Strikes', 'Coronavirus is spreading swiftly' ,"https://cointelegraph.com/news/rising-btc-price-justin-suns-harassment-suit-and-more-on-the-bad-crypto-podcast",)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

 if __name__ = '__main__':
    unittest.main()       