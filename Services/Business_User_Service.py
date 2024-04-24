from sqlalchemy.orm import Session

class BusinessUserService():
    def __init__(self, app):
        self.app = app


    
    def get_subcategory_names(self,product_type_id):
        session = self.app.Session()
        with session:
            result = session.query(self.app.map.Subcategory.subcategory_name, self.app.map.Subcategory.subcategory_id)\
                .join(self.app.map.ProductTypeSubcategories, self.app.map.Subcategory.subcategory_id == self.app.map.ProductTypeSubcategories.subcategory_id)\
                .filter(self.app.map.ProductTypeSubcategories.product_type_id == product_type_id)\
                .all()
            print(result)
        return result
    
    def get_values_based_on_subcategory(self, subcategory_ids):
        session = self.app.Session()
        Product = self.app.map.Product
        ProductSubcategories = self.app.map.ProductSubcategories
        with session:
            subquery1 = session.query(ProductSubcategories.product_id)\
                .filter(ProductSubcategories.subcategory_id == subcategory_ids[0])\
                .subquery().as_scalar()

            subquery2 = session.query(ProductSubcategories.product_id)\
                .filter(ProductSubcategories.subcategory_id == subcategory_ids[1])\
                .subquery().as_scalar()

            result = session.query(Product.product_name, Product.product_id)\
                .filter(Product.product_id.in_(subquery1), Product.product_id.in_(subquery2))\
                .all()
            

        return result
    
    def get_product_by_subcategory(self, subcategory_id):
        session = self.app.Session()
        Product = self.app.map.Product
        ProductSubcategories = self.app.map.ProductSubcategories
        with session:
            result = session.query( Product.product_name, Product.product_id)\
                .join(ProductSubcategories, Product.product_id == ProductSubcategories.product_id)\
                .filter(ProductSubcategories.subcategory_id == subcategory_id)\
                .all()
        return result
        

    def get_product_details(self, product_id):
        
        session = self.app.Session()
        Product = self.app.map.Product

        with session:

            result = session.query(Product.product_id, Product.product_name, Product.product_type_id, Product.product_description, Product.product_price)\
                .filter(Product.product_id == product_id)\
                .all()
            print(result)
        return result
    
    def create_order(self, order_data):
        session = self.app.Session()
        Order = self.app.map.Order
        with session:
            # Create a new order with the provided data
            order = Order(user_id=order_data['user_id'],
                           employee_id=order_data['employee_id'], 
                           business_id=order_data['business_id'],
                           order_date=order_data['order_date'])
            session.add(order)
            session.commit()
            order_id = order.order_id
        return order_id
    

    def create_order_details(self,order_details_data):

        print("*"*100)
        print(order_details_data)
        print("*"*100)
        session = self.app.Session()
        OrderDetails = self.app.map.OrderDetail
        with session:
            # Create a new order details with the provided data
            order_details = OrderDetails(order_id=order_details_data['order_id'], 
                                         product_id=order_details_data['product_id'], 
                                         product_type_id = order_details_data['product_type_id'])
            session.add(order_details)
            session.commit()
    
    def get_employee_details(self, user_id):
        session = self.app.Session()
        EmployeeBusiness = self.app.map.EmployeeBusiness
        with session:
            result = session.query(EmployeeBusiness.user_id, EmployeeBusiness.employee_id, EmployeeBusiness.business_id)\
                .filter(EmployeeBusiness.user_id == user_id)\
                .all()
        return result
    