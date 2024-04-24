
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector
from mysql.connector import Error

class Server_Management():

    def __init__(self,host_name, user_name, user_password, db_name = None):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
        

        self.connection = self.create_server_connection()

    


            
        
    def create_server_connection(self):
        connection = None
        try:
            print("\nCommencing MySQL connection...\n")
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name

            )
            
            print("MySQL connection successful\n")

            if connection.database is not None:
                print(f"Connected to database:  {connection.database}\n")
        


        except Error as err:
            print(f"Error: '{err}'")

            if 'Unknown database' in str(err):
                print("")
                raise Exception(f"Unknown database: '{self.db_name}' and create_db is set to False.")
            
                                
                                
            else:
                raise (f"ERROR:\n\n {err}")

        return connection
    
    
    
    




