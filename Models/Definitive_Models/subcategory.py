from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subcategory(Base):
    __tablename__ = 'Subcategories'

    subcategory_id = Column(Integer, primary_key=True)
    subcategory_name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('Categories.category_id'))
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, subcategory_name, category_id):
        self.subcategory_name = subcategory_name
        self.category_id = category_id

    def __repr__(self):
        return f"<Subcategory(subcategory_id='{self.subcategory_id}', subcategory_name='{self.subcategory_name}', category_id='{self.category_id}', created_at='{self.created_at}')>"