import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MOVIE_API_KEY = os.environ.get('BLOG_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:268231@localhost/blogposts'
    
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
