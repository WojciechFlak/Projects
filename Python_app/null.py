from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, DateTime)
import DB_connector
import App

from datetime import datetime

meta_data = MetaData()


users = Table('users', meta_data,

				Column('user_id', Integer(), primary_key = True),

				Column('username', String(15), nullable = False, unique = True),

				Column('email', String(150), nullable = False),

				Column('password', String(12), nullable = False),

				Column('created_on', DateTime(),default=datetime.now,nullable = False),

				Column('update_on', DateTime(), default=datetime.now, onupdate=datetime.now,nullable = False)

			)



engine = create_engine(App.db_engine)



try:

  conn = engine.connect()

  print('db connected')

  print('connection object is :{}'.format(conn))

except:

  print('db not connected')



meta_data.create_all(engine)



ins = users.insert().values(

		username="Vikas",

		email="V@gmail.com",

		password="123",

	)

print(str(ins))

print(ins.compile().params)

result = conn.execute(ins)

print('Last inserted key:')

print(result.inserted_primary_key)