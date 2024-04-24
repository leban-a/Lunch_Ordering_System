import tkinter as tk
from Views.base_view import BaseView

class LoginView(BaseView):
    def __init__(self, window, login_controller):
        super().__init__(window)
        self.window.geometry("500x200")
        self.login_controller = login_controller
        self.department_frame()
        self.window.title("Lunch App - Login")





    def department_frame(self):



        self.clear_window()
        frame = tk.Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')


        department = tk.Label(frame, text="Please select your department")
        department.grid(row=0, column=1, columnspan=3)

        department_admin = tk.Button(frame, text="Administration Admin", command=lambda: self.login_frame("Admin","Admin"))
        department_admin.grid(row=1, column=1,padx=10)

        department_admin = tk.Button(frame, text="Administration User", command=lambda: self.login_frame("Admin","User"))
        department_admin.grid(row=1, column=2,padx=10)

        department_business_user = tk.Button(frame, text="Business User", command=lambda: self.login_frame("Business","User"))
        department_business_user.grid(row=2, column=1,padx=10)

        department_business_admin = tk.Button(frame, text="Business Admin", command=lambda: self.login_frame("Business","Admin"))
        department_business_admin.grid(row=2, column=2, padx=10)


    def login_frame(self,user_type,user_role,login_failed = False):

        self.clear_window()
        frame = tk.Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        if user_type == "Admin" and user_role == "User":
            user_type_text = "Administration User"

        elif user_type == "Admin" and user_role == "Admin":
            user_type_text = "Administration Admin"

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



        login_button = tk.Button(frame, text="Login", command=lambda: self.login_controller.login(username_input.get(), password_input.get(), user_type, user_role))
        login_button.grid(row=3, column=2, columnspan=2)
        back_button = tk.Button(frame, text="Back", command=self.department_frame)
        back_button.grid(row=4, column=2, columnspan=2)

        if login_failed:
            login_failed_label = tk.Label(frame, text="Login Failed! Please try again", fg="red")
            login_failed_label.grid(row=5, column=2, columnspan=2)
