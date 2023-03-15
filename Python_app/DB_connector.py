import configparser
import os


from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

class Database:

    def __init__(self, db_settings_file):

        self.db_settings_file = db_settings_file
        # self.run_server()
        if not database_exists(self.get_engine().url):
            create_database(self.get_engine().url)
            print('Database {} created.'.format(self.database))
        else:
            print('Database {} already exists.'.format(self.database))

    @staticmethod
    def run_server():
        os.system('zsh ../SQL_DB/run_server.sh')


    def get_engine(self):

        config = configparser.ConfigParser()
        config.read(self.db_settings_file)

        self.host = config['postgresql']['host']
        self.user = config['postgresql']['user']
        self.port = config['postgresql']['port']
        self.database = config['postgresql']['database']
        __password = config['postgresql']['password']


        url = f'postgresql://{self.user}:{__password}@{self.host}:{self.port}/{self.database}'
        engine = create_engine(url)

        return engine





db_settings_file = '../DB.ini'


db = Database(db_settings_file)
#
# engine = db.get_engine()
#
# connection = engine.connect()
#
# connection.close()







