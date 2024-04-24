from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
    

class ProductSubcategory(Base):
    __tablename__ = 'ProductSubcategories'

    product_subcategory_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('Products.product_id'))
    subcategory_id = Column(Integer, ForeignKey('Subcategories.subcategory_id'))
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, product_id, subcategory_id):
        self.product_id = product_id
        self.subcategory_id = subcategory_id

    def __repr__(self):
        return f"<ProductSubcategory(product_subcategory_id='{self.product_subcategory_id}', product_id='{self.product_id}', subcategory_id='{self.subcategory_id}', created_at='{self.created_at}')>" 