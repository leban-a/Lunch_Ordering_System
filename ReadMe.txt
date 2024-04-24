
Libaries Needed: 

sqlalchemy
tkinter
mysql


How to use:
This application relies on a SQL Server Connection. Program is currently Set to work on a local server:
Used SQL-Workbench to interact with SQL



Application will connect to the server using the following credentials unless changed in main.py
            db_name='DatabaseTest',
            host_name = 'localhost',
            user_name = 'root', 
            user_password = 'password', 


Database and tables will be automatically created and then populated. Rules can be adjusted in set_up.py or main.py
Tables.py and Data.py store SQL Create and SQL Insert requess.


Testing:  
All users can login, result shown in termianl, for Business Admin,  Admin and Admin. User Login Details Located in Data.py
BusinessUsers can create orders,  limited to 1 order per calandar day, 14day look ahaead. 




### Development - Corporate Lunch System: 

This branch aims build on the features established in the meal deal application: 

It will included two key stake holder Groups: Business and Administration: broken down in two subsets Users and Admins 

The application use case:

This application would be ideal for a organisation that provides lunches for their staff.
This could be used for both in-house and third party lunch suppliers. 


An admin: 
Will be able manage all the users, orders and inventory, as-well as generate reports

An employee:
Will be able to add, modify, or delete their meal order.

A business: will be able t0 manage orders, manager users within their business and generate reports. 

This Project will aim to provide a GUI for the various user views.
The application will incorporate a SQL Database System, implemented and queried using python.



Development:

The Application will be modelled using the MVC (Model View Controller) Development Process With a Serice Layer:


├── Controllers/
│   ├── __init__.py
│   ├── business_user_controller.py
│   └── login_controller.py
│
├── Models/
│   ├── Definitive_Models/
│   │   ├── business.py
│   │   ├── business_rate.py
│   │   ├── employee_business.py
│   │   ├── inventory.py
│   │   ├── order.py
│   │   ├── order_details.py
│   │   ├── product.py
│   │   ├── product_subcategory.py
│   │   ├── product_type.py
│   │   ├── subcategory.py
│   │   └── user.py
│   ├── Model_Mapping.py
│   └── __init__.py
│
├── Services/
│   ├── Business_User_Service.py
│   ├── Database/
│   │   ├── Database_Tables/
│   │   │   ├── Data.py
│   │   │   └── Tables.py
│   │   ├── SQL_Database_Management.py
│   │   ├── SQL_Database_Setup.py
│   │   ├── SQL_Server_Management.py
│   │   ├── Setup.py
│   │   └── __init__.py
│   ├── User_Service.py
│   └── __init__.py
│
├── Views/
│   ├── __init__.py
│   ├── base_view.py
│   ├── business_user_view.py
│   └── login_view.py
│
├── main.py
├── ReadMe.txt


#####
Previous Scopes - Moved to Legacy Files
#####



### Meal Deal

This codebase implements a meal deal calculator that allows users to create customized meal deals consisting of a main dish, a snack, and a drink. The meal deal options are predefined, and the user can choose from a variety of items available in each category.

#### Methods Used:

1. **main()**: This function serves as the main entry point for the meal deal calculator. It prompts the user to select items for each meal deal category, calculates the total cost of the meal deal including any applicable discounts and sugar tax, and then prints the details of the meal deal.

2. **step_through_database(keys, database)**: This function displays the available options for a given category from the database and checks if any products are listed. It iterates through each key in the database, prints the details of the products including their prices and descriptions, and returns a boolean indicating if any products are listed. A product is defined as listed when its displayed to the user at this stage the user can make thier final selection for a given category. 


3. **get_input(database)**: This function prompts the user for input and returns their selection if it exists in the provided database. It loops indefinitely until a valid input is received, checking if the input exists in the database before returning it.

4. **get_database(keys, database)**: This function retrieves data from the database based on a list of keys. It iterates through each key in the list, updating the database with the data corresponding to the current key, and returns the final database after all keys are processed.

5. **get_selection(target)**: This function recursively prompts the user to select an item from a given category until a valid selection is made. It initializes a list of keys with the initial category, retrieves the corresponding data from the database, and enters a loop until a valid selection is made. Within the loop, it displays the available options for the current category, prompts the user for input, and updates the keys list with the user's selection. After each iteration, it updates the working database with the new category data based on the user's input. If a valid product is selected, it returns the list of keys representing the chosen products.


