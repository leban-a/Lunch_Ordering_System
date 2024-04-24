from Services.Database_Tables.Tables import *
from Services.Database_Tables.Data import *


class Database_Setup():

    def __init__(self, execute_query, connection,  tables = False, data = False):

        if tables:
            self.create_database_tables(execute_query, connection)
        if data:
            self.populate_database_tables(execute_query, connection)
            


    def create_database_tables(self, execute_query, connection):

        # Create the user table
        execute_query(  create_user_table)

        # Create the business table
        execute_query( create_business_table)

        # Create the employee table
        execute_query( create_employee_business_table)

        # Create the product type table
        execute_query( create_product_type_table)

        # Create the product table
        execute_query( create_product_table)

        # Create the inventory table
        execute_query( create_invertory_table)

        # Create the subcategories table
        execute_query( create_subcategories_table)

        # Create the product subcategories table
        execute_query( create_product_subcategories_table)

        # Create the business rates table
        execute_query( create_business_rates_table)

        # Create the order table
        execute_query( create_orders_table)

        # Create the order details table
        execute_query( create_order_details_table)



    def populate_database_tables(self, execute_query, connection):

        # Populate the user table
        execute_query( pop_user_table)

        # Populate the business table
        execute_query( pop_business_table)

        # Populate the employee table
        execute_query( pop_employee_business_table)

        # Populate the product type table
        execute_query( pop_product_type_table)

        # Populate the product table
        execute_query( pop_product_table)

        # Populate the inventory table
        execute_query( pop_inventory_table)

        # Populate the subcategories table
        execute_query( pop_subcategories_table)

        # Populate the product subcategories table
        execute_query( pop_product_subcategories_table)

        # Populate the business rates table
        execute_query( pop_business_rates_table)


