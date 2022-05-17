import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    QUOTE_API_KEY = os.environ.get('QUOTE_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:268231@localhost/blogposts'
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
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
