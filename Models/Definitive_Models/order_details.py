from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class OrderDetail(Base):

    __tablename__ = 'OrderDetails'

    order_detail_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('Orders.order_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('Products.product_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    order_detail_created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, order_id, product_id, quantity, price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"<OrderDetail(order_detail_id='{self.order_detail_id}', order_id='{self.order_id}', product_id='{self.product_id}', quantity='{self.quantity}', price='{self.price}')>"