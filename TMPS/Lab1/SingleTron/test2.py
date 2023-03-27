import database_connection

def read():
    db = database_connection.Database.get_instance()
    db.select_data()