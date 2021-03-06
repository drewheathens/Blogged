import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or '1234'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    API_BASE_URL='http://quotes.stormconsultancy.co.uk/{}.json'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://evans:wewe@localhost/articles'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://evans:wewe@localhost/articles'
    DEBUG = True



config_options ={
    'development':DevConfig,
    'production':ProdConfig
}
