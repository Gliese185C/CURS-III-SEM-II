import database_connection

def write(string):
    db = database_connection.Database.get_instance()
    db.insert_data(string)