from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base 


Base = declarative_base() 

class EmployeeBusiness(Base): 
    __tablename__ = 'EmployeeBusiness' 

    employee_id = Column(Integer, primary_key=True) 
    business_id = Column(Integer, ForeignKey('Businesses.business_id')) 
    user_id = Column(Integer, ForeignKey('Users.user_id')) 
    employee_name = Column(String(50), nullable=False) 
    employee_last_name = Column(String(50), nullable=False) 
    employee_department = Column(String(50), nullable=False) 
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP') 

    def __init__(self, business_id, user_id, employee_name, employee_last_name, employee_department): 
        self.business_id = business_id 
        self.user_id = user_id 
        self.employee_name = employee_name 
        self.employee_last_name = employee_last_name 
        self.employee_department = employee_department 

    def __repr__(self): 
        return f"<EmployeeBusiness(employee_id='{self.employee_id}', business_id='{self.business_id}', user_id='{self.user_id}', employee_name='{self.employee_name}', employee_last_name='{self.employee_last_name}', employee_department='{self.employee_department}')>"