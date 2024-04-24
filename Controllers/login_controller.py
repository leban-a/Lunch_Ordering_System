

class LoginController:
    def __init__(self, app, user_service, view=None):
        self.app = app
        self.user_service = user_service
        self.view = view

    def login(self, username, password, user_type, user_role):
        user_id = self.user_service.get_user_id(username, password, user_type, user_role)
        print(user_id)

        if user_id:
            print("Login successful")
            
            self.app.logged_in_user = user_id
            self.app.transition_to(self.app.states[f'{user_type}_{user_role}'])   
        else:
            print("Login failed")
            self.view.login_frame(user_type, user_role, login_failed=True)