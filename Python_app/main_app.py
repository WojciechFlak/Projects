import customtkinter

import DB_connector
import GUI.GUI2


if __name__ == '__main__':

    settings_file = '../SQL_DB/DB.ini'
    schema = '../SQL_DB/create_tables.sql'

    db = DB_connector.Database(settings_file, schema)
    db.run_server()
    db.create_db()
    db.db_schema_creation()


    # db.insert('dddd', 'rrrrr')

    root = customtkinter.CTk()
    app_gui = GUI.GUI2.App_GUI(root)
    root.mainloop()

    # TODO: reading and writing to db with gui

    db.stop_server()
