from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    product_type_id = Column(Integer, ForeignKey('ProductTypes.product_type_id'))
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, product_name, product_type_id, price):
        self.product_name = product_name
        self.product_type_id = product_type_id
        self.price = price

    def __repr__(self):
        return f"<Product(product_id='{self.product_id}', product_name='{self.product_name}', product_type_id='{self.product_type_id}', price='{self.price}', created_at='{self.created_at}')>"
    