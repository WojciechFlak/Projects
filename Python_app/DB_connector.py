import configparser
import os


from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database


class Database:

    def __init__(self, db_settings_file):

        self.db_settings_file = db_settings_file

        config = configparser.ConfigParser()
        config.read(self.db_settings_file)

        self.host = config['postgresql']['host']
        self.user = config['postgresql']['user']
        self.port = config['postgresql']['port']
        self.database = config['postgresql']['database']
        self.__password = config['postgresql']['password']
        self.url = f'postgresql://{self.user}:{self.__password}@{self.host}:{self.port}/{self.database}'

    def create_db(self):

        if not database_exists(self.url):
            create_database(self.url)
            print('Database {} created.'.format(self.database))
        else:
            print('Database {} already exists.'.format(self.database))

    @staticmethod
    def run_server():
        os.system(f'zsh ../SQL_DB/run_server.sh')

    @staticmethod
    def stop_server():
        os.system('zsh ../SQL_DB/stop_server.sh')

    def get_engine(self):
        engine = create_engine(self.url)
        return engine


settings_file = '../DB.ini'

db = Database(settings_file)
db.run_server()
db.create_db()
db_engine = db.get_engine()
connection = db_engine.connect()
connection.close()

db.stop_server()
