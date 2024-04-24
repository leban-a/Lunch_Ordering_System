from sqlalchemy.orm import Session

class UserService:
    def __init__(self , app):
        self.app = app
        

    def get_user_id(self, username: str, password: str, user_type: str, user_role: str):
        session = self.app.Session()  # Call the sessionmaker instance to get a Session object
        with session:  # Use the Session object as a context manager
            user = session.query(self.app.map.User).filter_by(
                username=username,
                password=password,  # Note: You should hash passwords, not store them in plain text
                user_type=user_type,
                role=user_role
            ).first()

            return user.user_id if user else None