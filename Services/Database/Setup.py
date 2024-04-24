# We will use this class to establish connections to the SQL Server and Database

from Services.Database.SQL_Database_Management import Database_Management
from Services.Database.SQL_Database_Setup import Database_Setup  
from Services.Database.SQL_Server_Management import Server_Management



class Establish_Connections():

    def __init__(self, host_name = 'localhost', user_name = 'root', user_password = 'password', db_name = 'LAPLA1622', create_db = True, create_tables = True, create_data = True):

        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name

    

        # Create a new SQL Server Management object
        self.sql_server_manager = Server_Management(host_name, user_name, user_password, None if create_db else db_name) 
        # Create a new SQL Database Management object
        self.sql_database_manager = Database_Management(self.sql_server_manager, db_name if create_db else None) 
        # Create a new SQL Database Setup object

        if create_db and (create_tables or create_data):
            sql_database_setup = Database_Setup(self.sql_database_manager.execute_query, self.sql_database_manager.connection, create_tables, create_data)
        
        self.connection = self.sql_server_manager.connection     


        self.engine = self.sql_database_manager.engine   

        print("\n\nConnections Established\n")



