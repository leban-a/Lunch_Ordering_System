from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    user_type = Column(Enum('Admin', 'Business'), nullable=False)
    role = Column(Enum('User', 'Admin'), nullable=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')
    last_login = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, username, password, email, user_type, role):
        self.username = username
        self.password = password
        self.email = email
        self.user_type = user_type
        self.role = role

    def __repr__(self):
        return f"<User(user_id='{self.user_id}', username='{self.username}', email='{self.email}', user_type='{self.user_type}', role='{self.role}')>"
    


