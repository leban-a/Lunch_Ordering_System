from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

class Model_Mapper():
    def __init__(self, engine):
        self.engine = engine    
        self.map_models()

    def map_models(self):

        print("\nMapping models...\n")
        # Create the connection engine
        engine = self.engine

        # Create a base class using automap
        self.Base = automap_base()

        # Reflect the tables
        self.Base.prepare(engine, reflect=True)
        print("Tables reflected:\n")
        print('\n'.join(self.Base.classes.keys()))
        # Now you can access your models using the classes that automap created
        self.User = self.Base.classes.Users
        self.Business = self.Base.classes.Businesses
        self.EmployeeBusiness = self.Base.classes.EmployeeBusiness
        self.ProductType = self.Base.classes.ProductTypes
        self.Product = self.Base.classes.Products
        self.Inventory = self.Base.classes.Inventory
        self.Subcategory = self.Base.classes.Subcategories
        self.BusinessRate = self.Base.classes.BusinessRates
        self.Order = self.Base.classes.Orders
        self.OrderDetail = self.Base.classes.OrderDetails
        self.ProductSubcategories = self.Base.classes.ProductSubcategories
        self.ProductTypeSubcategories = self.Base.classes.ProductTypeSubcategories
        
        
        print("\nModels mapped successfully\n")