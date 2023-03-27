import sqlite3
import psycopg2


# Abstract factory
class DBFactory:
    def create_connection(self):
        pass

    def create_cursor(self):
        pass

# Concrete factory for SQLite
class SQLiteFactory(DBFactory):
    def create_connection(self):
        return sqlite3.connect('database.db')

    def create_cursor(self):
        return self.create_connection().cursor()


# Concrete factory for PostgreSQL
class PostgresFactory(DBFactory):
    def create_connection(self):
        return psycopg2.connect(host='localhost', user='user', password='password', dbname='database')

    def create_cursor(self):
        return self.create_connection().cursor()


# Client code
def connect_to_database(db_type):
    if db_type == 'sqlite':
        factory = SQLiteFactory()
    elif db_type == 'postgres':
        factory = PostgresFactory()
    else:
        raise ValueError('Unsupported database type: %s' % db_type)

    connection = factory.create_connection()
    cursor = factory.create_cursor()

    return connection, cursor

