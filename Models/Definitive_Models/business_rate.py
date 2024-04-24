from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BusinessRate(Base):
    __tablename__ = 'BusinessRates'

    business_rate_id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey('Businesses.business_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    rate = Column(Integer, nullable=False)
    comment = Column(String(50), nullable=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, business_id, user_id, rate, comment):
        self.business_id = business_id
        self.user_id = user_id
        self.rate = rate
        self.comment = comment

    def __repr__(self):
        return f"<BusinessRate(business_rate_id='{self.business_rate_id}', business_id='{self.business_id}', user_id='{self.user_id}', rate='{self.rate}', comment='{self.comment}')>"