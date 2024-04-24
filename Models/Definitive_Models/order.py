from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):  
    __tablename__ = 'Orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('EmployeeBusiness.employee_id'), nullable=False)
    business_id = Column(Integer, ForeignKey('Businesses.business_id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default='CURRENT_TIMESTAMP')
    order_created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, user_id, employee_id, business_id, order_date):
        self.user_id = user_id
        self.employee_id = employee_id
        self.business_id = business_id
        self.order_date = order_date
        

    def __repr__(self):
        return f"<Order(order_id='{self.order_id}', user_id='{self.user_id}', employee_id='{self.employee_id}', business_id='{self.business_id}', order_date='{self.order_date}')>"
