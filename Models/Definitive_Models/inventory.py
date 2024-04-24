from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base


Base    = declarative_base()

class Inventory(base): 
    __tablename__ = 'Inventory' 

    inventory_id = Column(Integer, primary_key=True) 
    product_id = Column(Integer, ForeignKey('Products.product_id')) 
    quantity = Column(Integer, nullable=False) 
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP') 

    def __init__(self, product_id, quantity): 
        self.product_id = product_id 
        self.quantity = quantity 

    def __repr__(self): 
        return f"<Inventory(inventory_id='{self.inventory_id}', product_id='{self.product_id}', quantity='{self.quantity}', created_at='{self.created_at}')>"

