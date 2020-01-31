class config:
    '''
    general configuration parent class
    '''
    pass
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-12-31&sortBy=publishedAt&apiKey=API_KEY'

class ProdConfig(config):
    '''
    production configuration child class
    
    Args:
        config: The parent configuration class with general configuration settings
    ''' 
    pass

class DevConfig(config):
    '''
    development configuration child class

    Args:
         config: The parent configuration class with general configuration settings
    '''

    DEBUG = True     