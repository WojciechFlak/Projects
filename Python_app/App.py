from DB_connector import *

settings_file = '../DB.ini'
schema_file = '../SQL_DB/create_tables.sql'

db = Database(settings_file)
db.run_server()
db.create_db()
db.db_schema(schema_file)

db_engine = db.get_engine()
connection = db_engine.connect()

base.metadata.create_all(db_engine)


connection.close()

db.stop_server()
