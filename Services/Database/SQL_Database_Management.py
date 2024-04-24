from mysql.connector import Error
from sqlalchemy import create_engine

class Database_Management:
    def __init__(self, server_manager, db_name=None):

        self.db_name = db_name
        self.server_manager = server_manager
        
        self.connection = server_manager.connection

        if self.connection.database is None and db_name is not None:
            self.create_database(db_name)

        elif db_name is None and self.connection.database is None:
            raise Exception("Database name is required")
    
    
        self.server_manager.db_name = self.connection.database

        self.engine = self.create_sqlalchemy_engine()
        

        
    

    def create_database(self, db_name):

        print("Attempting to create database...\n")
        cursor = self.connection.cursor()   
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()  # returns a list of all databases

        if db_name in str(databases):
            print(f"The database {db_name} already exists.\n")
            self.connection.database = db_name
            print(f"Connected to database: {self.connection.database}\n")

        else:
        
            try:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")


                print("Database created successfully\n")
                self.connection.database = db_name
                self.db_name = self.connection.database
                print(f"Connected to database: {self.connection.database}\n")

                
            except Error as err:
                print(f"Error: '{err}'")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def read_query(self, query, params=None):  
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def create_sqlalchemy_engine(self):
        engine = create_engine(f"mysql+pymysql://{self.server_manager.user_name}:{self.server_manager.user_password}@{self.server_manager.host_name}/{self.db_name if self.db_name is not None else self.connection.database}")
        return engine



