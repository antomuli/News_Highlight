class config:
    '''
    general configuration parent class
    '''
    pass

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