create_user_table = """
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    user_type ENUM('Admin', 'Business') NOT NULL,
    role ENUM('User', 'Admin') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_business_table = """
CREATE TABLE Businesses (
    business_id INT AUTO_INCREMENT PRIMARY KEY,
    business_name VARCHAR(50) NOT NULL UNIQUE,
    business_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_employee_business_table = """
CREATE TABLE EmployeeBusiness (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    business_id INT,
    user_id INT NOT NULL,
    employee_name VARCHAR(50) NOT NULL,
    employee_last_name VARCHAR(50) NOT NULL,
    employee_department VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (business_id) REFERENCES Businesses(business_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    CONSTRAINT unique_employee UNIQUE (business_id, user_id, employee_name, employee_last_name)
);
"""


create_product_type_table = """
CREATE TABLE ProductTypes (
    product_type_id INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (product_type)
);
"""

create_product_table = """
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    product_type_id INT NOT NULL,
    product_description VARCHAR(255),
    product_price DECIMAL(10, 2) NOT NULL,
    product_sugar_taxed BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (product_name, product_type_id, product_price, product_description),
    FOREIGN KEY (product_type_id) REFERENCES ProductTypes(product_type_id)
);
"""


create_invertory_table = """
CREATE TABLE Inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    UNIQUE (product_id)
);
"""



create_subcategories_table = """
CREATE TABLE Subcategories (
    subcategory_id INT AUTO_INCREMENT PRIMARY KEY,
    subcategory_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (subcategory_name)
);
"""

create_product_subcategories_table = """
CREATE TABLE ProductSubcategories (
    product_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (subcategory_id) REFERENCES Subcategories(subcategory_id),
    UNIQUE (product_id, subcategory_id)
);
"""


create_business_rates_table = """
CREATE TABLE BusinessRates (
    business_rate_id INT AUTO_INCREMENT PRIMARY KEY,
    business_id INT NOT NULL,
    tax_rate DECIMAL(10, 2) NOT NULL,
    sugar_tax_rate DECIMAL(10, 2) NOT NULL,
    business_discount_rate DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (business_id) REFERENCES Businesses(business_id),
    UNIQUE (business_id)
);
"""

create_orders_table = """
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    employee_id INT NOT NULL,
    business_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES EmployeeBusiness(employee_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (business_id) REFERENCES Businesses(business_id),
    UNIQUE (user_id, order_date)
);
"""

create_order_details_table = """
CREATE TABLE OrderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    product_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    UNIQUE (order_id, product_id)
    );
"""
