import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db?check_same_thread=False')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['testjuldovga@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['de', 'rus']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or '627c2b648e5f479ca25d3377ede40086'
