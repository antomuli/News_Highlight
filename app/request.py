from app import app
from urllib.request,json
from.models import news

News = news>

#Getting API key
api_key = app.config['NEWS_API_KEY']

#Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
  '''
  Function that gets the json response to our url request
  '''
  get_news_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_source = None

    if get_news_response['source']:
      news_source_list = get_news_response['source']
      news_source = process_source(news_source_list)

def process_source(news_list):
    '''
    Function  that processes the news source and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_source: A list of news objects
    '''
    news_source = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        description = news_item.get('description')
        author = news_item.get('author')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')

        if poster:
            news_object = News(id,title,author,description, author, content, publishedAt)
            movie_results.append(movie_object)

 return news_source   