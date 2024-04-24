import tkinter as tk

from Services.SQL_Server_Management import  Server_Management as SQL_Server_Manager
from Services.SQL_Database_Management import Database_Management as SQL_Database_Manager
from Services.SQL_Database_Setup import Database_Setup as SQL_Database_Setup



class User_Login:

    def __init__(self, read_query, connection, window):

        self.read_query = read_query
        self.connection = connection
        self.window = window

        self.logged_in_user = None

        self.department_frame()
        
        
    def get_user_ID(self, username, password, user_type, user_role):

        query = "SELECT user_ID FROM Users WHERE username = %s AND password = %s AND user_type = %s AND role = %s"
        params = (username, password, user_type, user_role)

        
        return self.read_query(query, params)







    def clear_frame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def clear_window(self,):
        for widget in self.window.winfo_children():
            widget.destroy()

    def department_frame(self):

        self.clear_window()
        frame = tk.Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')


        department = tk.Label(frame, text="Please select your department")
        department.grid(row=0, column=1, columnspan=3)

        department_admin = tk.Button(frame, text="Admin", command=lambda: self.login_frame("Admin","Admin"))
        department_admin.grid(row=1, column=1,padx=10)

        department_business_user = tk.Button(frame, text="Business User", command=lambda: self.login_frame("Business","User"))
        department_business_user.grid(row=1, column=2,padx=10)

        department_business_admin = tk.Button(frame, text="Business Admin", command=lambda: self.login_frame("Business","Admin"))
        department_business_admin.grid(row=1, column=3, padx=10)


    def login_frame(self, user_type,user_role,login_failed = False):

        self.clear_window()
        frame = tk.Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        if user_type == "Admin":
            user_type_text = "Admin"
        elif user_type == "Business" and user_role == "User":
            user_type_text = "Business User"
        elif user_type == "Business" and user_role == "Admin":
            user_type_text = "Business Admin"

        user_type_label = tk.Label(frame, text=f"{user_type_text} Login")
        user_type_label.grid(row=0, column=1, columnspan=2) 



        
        username_label = tk.Label(frame, text="Username")
        username_label.grid(row=1, column=1)
        username_input = tk.Entry(frame, width=20)
        username_input.grid(row=1, column=2)

        password_label = tk.Label(frame, text="Password")
        password_label.grid(row=2, column=1)
        password_input = tk.Entry(frame, width=20)
        password_input.grid(row=2, column=2)



        login_button = tk.Button(frame, text="Login", command=lambda: self.login(username_input.get(), password_input.get(), user_type, user_role))
        login_button.grid(row=3, column=2, columnspan=2)
        back_button = tk.Button(frame, text="Back", command= self.department_frame)
        back_button.grid(row=4, column=2, columnspan=2)

        if login_failed:
            login_failed_label = tk.Label(frame, text="Login Failed! Please try again", fg="red")
            login_failed_label.grid(row=5, column=2, columnspan=2)



    def login(self,username, password, user_type, user_role):
        

        if self.get_user_ID(username, password, user_type, user_role):
            print("Login successful")
            logged_in_user = self.get_user_ID(username, password, user_type, user_role)[0][0]
        else:
            print("Login failed")
            self.login_frame(user_type,user_role, login_failed=True)
    

def main():


    host_name = 'localhost' # Change this to the hostname of your MySQL server
    user_name = 'root' # Change this to the username you use to connect to your MySQL server
    user_password = 'password' # Change this to the password you use to connect to your MySQL server
    db_name = 'LAPLA1622' # Change this to the name of the database you want to use or create

    create_db = True  # Set to True to create a new database with the name db_name

    # Create a new SQL Server Management object
    sql_server_manager = SQL_Server_Manager(host_name, user_name, user_password, None if create_db else db_name) 

    # Create a new SQL Database Management object
    sql_database_manager = SQL_Database_Manager(sql_server_manager.connection, db_name if create_db else None) 


    

    create_tables = True # Set to True to create the tables in the database
    create_data = True  # Set to True to populate the tables with data create_tables must be True to populate the tables

    sql_database_setup = SQL_Database_Setup(sql_database_manager.execute_query, sql_database_manager.connection, create_tables, create_data)
    


    
    window = tk.Tk()
    window.geometry("500x200")
    

    login = User_Login(sql_database_manager.read_query, sql_database_manager.connection, window)


    
    window.mainloop()
    
    

    
if __name__ == "__main__":
    main()
    