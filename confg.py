import os  

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'your-storage-key'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
