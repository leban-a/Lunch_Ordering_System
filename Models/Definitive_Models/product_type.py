from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class ProductType(Base):
    __tablename__ = 'ProductTypes'

    product_type_id = Column(Integer, primary_key=True)
    product_type = Column(String(255), nullable=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, product_type):
        self.product_type = product_type

    def __repr__(self):
        return f"<ProductType(product_type_id='{self.product_type_id}', product_type='{self.product_type}', created_at='{self.created_at}')>"