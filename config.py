SQLITE = "sqlite:///project.db"
POSGRESQL = 'postgresql+psycopg2://postgres:123456@localhost:5432/codesoft_db'

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    SQLALCHEMY_DATABASE_URI = POSGRESQL

    CKEDITOR_PKG_TYPE = 'basic'