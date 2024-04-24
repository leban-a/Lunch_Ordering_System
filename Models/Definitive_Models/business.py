from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Business(Base):
    __tablename__ = 'Businesses'

    business_id = Column(Integer, primary_key=True)
    business_name = Column(String(50), unique=True, nullable=False)
    business_type = Column(String(50), nullable=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, business_name, business_type):
        self.business_name = business_name
        self.business_type = business_type

    def __repr__(self):
        return f"<Business(business_id='{self.business_id}', business_name='{self.business_name}', business_type='{self.business_type}')>"