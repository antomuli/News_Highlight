import unittest
from ..models import news

News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
      '''
      Set up method that will run before every test
      '''
      self.new_news = News("abc-News", "ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com","https://abcnews.go.com","general","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main() 

 