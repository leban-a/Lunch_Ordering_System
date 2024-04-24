import json
import tkinter as tk


window = tk.Tk()
window.geometry("500x200")



def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def department_frame():

    clear_window()
    frame = tk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')


    department = tk.Label(frame, text="Please select your department")
    department.grid(row=0, column=1, columnspan=3)

    department_admin = tk.Button(frame, text="Admin", command=lambda: login_frame("admin"))
    department_admin.grid(row=1, column=1,padx=10)

    department_business_user = tk.Button(frame, text="Business User", command=lambda: login_frame("business_user"))
    department_business_user.grid(row=1, column=2,padx=10)

    department_business_admin = tk.Button(frame, text="Business Admin", command=lambda: login_frame("business_admin"))
    department_business_admin.grid(row=1, column=3, padx=10)


def login_frame(user_type, login_failed = False):

    clear_window()
    frame = tk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    if user_type == "admin":
        user_type_text = "Admin"
    elif user_type == "business_user":
        user_type_text = "Business User"
    elif user_type == "business_admin":
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



    login_button = tk.Button(frame, text="Login", command=lambda: login(username_input.get(), password_input.get(), user_type))
    login_button.grid(row=3, column=2, columnspan=2)
    back_button = tk.Button(frame, text="Back", command=department_frame)
    back_button.grid(row=4, column=2, columnspan=2)

    if login_failed:
        login_failed_label = tk.Label(frame, text="Login Failed! Please try again", fg="red")
        login_failed_label.grid(row=5, column=2, columnspan=2)


def load_user_data():
    with open("backend_user_database.json", "r") as file:
        return json.load(file)


def login(username, password, user_type):
    
    user_data = load_user_data()

    for user_profile in user_data[user_type]:
        if user_profile["Username"] == username and user_profile["Password"] == password:
            print("Login successful")
            return
    else:
        print("Login failed")
        login_frame(user_type, login_failed=True)
    

def main():



    department_frame()

    
if __name__ == "__main__":
    main()
    window.mainloop()
