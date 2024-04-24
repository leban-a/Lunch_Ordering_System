from mysql.connector import Error

class Database_Management:
    def __init__(self, connection, db_name=None):
        
        self.connection = connection

        if self.connection.database is None and db_name is not None:
            self.create_database(db_name)

        
    

    def create_database(self, db_name):

        print("Creating database...\n")
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




    

