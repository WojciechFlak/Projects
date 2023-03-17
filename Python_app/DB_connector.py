import configparser
import os


from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, MetaData, DateTime
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
        os.system('zsh ../SQL_DB/run_server.sh')

    @staticmethod
    def stop_server():
        os.system('zsh ../SQL_DB/stop_server.sh')

    def get_engine(self):
        engine = create_engine(self.url)
        return engine


    def db_schema(self, db_schema_file):
        os.system(f'psql  -d {self.database} -a -f {db_schema_file}')  # TODO silnikiem a nie psql



from datetime import datetime
settings_file = '../DB.ini'
meta_data = MetaData()
db = Database(settings_file)
db_engine = db.get_engine()


users = Table('users', meta_data,

				Column('user_id', Integer(), primary_key = True, autoincrement=True),

				Column('username', String(15), nullable = False, unique = True),

				Column('email', String(150), nullable = False),

				Column('password', String(12), nullable = False),

				Column('created_on', DateTime(),default=datetime.now,nullable = False),

				Column('update_on', DateTime(), default=datetime.now, onupdate=datetime.now,nullable = False)

			)






try:

  conn = db_engine.connect()

  print('db connected')

  print('connection object is :{}'.format(conn))

except:

  print('db not connected')



meta_data.create_all(db_engine)



ins = users.insert().values(

		username="Vikassd",

		email="V@gmail.com",

		password="123",

	)

print(str(ins))

print(ins.compile().params)

result = conn.execute(ins)
conn.commit()

print('Last inserted key:')

print(result.inserted_primary_key)
