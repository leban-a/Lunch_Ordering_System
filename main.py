import tkinter as tk
from sqlalchemy.orm import sessionmaker


from Views.login_view import LoginView
from Views.business_user_view import BusinessUserView

from Controllers.login_controller import LoginController
from Controllers.business_user_controller import BusinessUserController


from Services.Database.Setup import Establish_Connections
from Models.Model_Mapping import Model_Mapper

from Services.User_Service import UserService
from Services.Business_User_Service import BusinessUserService




class Application:
    def __init__(self):
        self.window = tk.Tk()

        self.screen_size = "500x500"
        self.window.geometry(self.screen_size)
        self.state = None

        self.server = Establish_Connections(
            db_name='SkillsNetworkTest', 
            create_db=True, 
            create_tables=True, 
            create_data=True)
        
        self.logged_in_user = None


        self.states = {
            'login': LoginState(self),
            'Business_User': BusinessUserState(self),
            'Business_Admin': BusinessAdminState(self),
            'Admin_Admin': AdminAdminState(self),
            'Admin_User': AdminUserState(self)
        }
        self.connection = self.server.connection


        self.engine = self.server.engine   


        self.Session = sessionmaker(bind=self.engine)
        self.map = Model_Mapper(self.engine)


        self.user_service = UserService(self)

        self.business_user_service = BusinessUserService(self)


    def run(self):
        self.transition_to(LoginState(self))
        self.window.mainloop()

    def transition_to(self, state):
        self.state = state
        self.state.enter()

class State:
    def enter(self):
        pass


class LoginState(State):
    def __init__(self, app):
        self.app = app

    def enter(self):
        self.controller = LoginController(self.app, self.app.user_service)
        self.view = LoginView(self.app.window, self.controller)

        self.controller.view = self.view

class BusinessUserState(State):
    def __init__(self, app):
        self.app = app
        

    def enter(self):
        self.controller = BusinessUserController(self.app, self.app.business_user_service)
        self.view = BusinessUserView(self.app.window, self.controller)

        self.controller.view = self.view

class BusinessAdminState(State):
    def __init__(self, app):
        self.app = app
        

    def enter(self):
        print("Business Admin State")

class AdminAdminState(State):
    def __init__(self, app):
        self.app = app
        

    def enter(self):
        print("Admin Admin State")

class AdminUserState(State):
    def __init__(self, app):
        self.app = app
        

    def enter(self):
        print("Admin User State")



# define other states as needed...

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()