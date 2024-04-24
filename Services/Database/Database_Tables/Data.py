pop_user_table = """
INSERT INTO Users (username, password, email, user_type, role, created_at, last_login) VALUES
('john_doe', 'password123', 'john.doe@example.com', 'Admin', 'Admin', '2024-04-18 12:00:00', '2024-04-18 12:00:00'),
('jane_smith', 'letmein', 'jane.smith@example.com', 'Business', 'User', '2024-04-18 12:15:00', '2024-04-18 12:15:00'),
('alex_wong', 'securepwd', 'alex.wong@example.com', 'Business', 'User', '2024-04-18 12:30:00', '2024-04-18 12:30:00'),
('emma_jones', 'password123', 'emma.jones@example.com', 'Business', 'Admin', '2024-04-18 12:45:00', '2024-04-18 12:45:00'),
('michael_davis', 'password123', 'michael.davis@example.com', 'Admin', 'User', '2024-04-18 13:00:00', '2024-04-18 13:00:00');

"""

pop_business_table = """
INSERT INTO Businesses (business_name, business_type, created_at) VALUES
('Tech Solutions Inc.', 'Technology', '2024-04-18 12:00:00'),
('Gourmet Eats LLC', 'Food & Beverage', '2024-04-18 12:15:00'),
('Green Gardens Ltd.', 'Landscaping', '2024-04-18 12:30:00'),
('Fashion Trends Co.', 'Retail', '2024-04-18 12:45:00'),
('Smith & Associates', 'Consulting', '2024-04-18 13:00:00');
"""

pop_employee_business_table = """
INSERT INTO EmployeeBusiness (business_id, user_id, employee_name, employee_last_name, employee_department, created_at) VALUES
(1, 2, 'Jane', 'Smith', 'Marketing', '2024-04-18 12:15:00'),
(2, 3, 'Alex', 'Wong', 'Finance', '2024-04-18 12:30:00'),
(3, 4, 'Emma', 'Jones', 'HR', '2024-04-18 12:45:00')
"""


pop_product_type_table = """
INSERT INTO ProductTypes (product_type, created_at) VALUES

('Main', '2024-04-18 12:15:00'),
('Snack', '2024-04-18 12:30:00'),
('Drink', '2024-04-18 12:00:00');
"""


pop_product_table = """
INSERT INTO Products (product_name, product_type_id, product_description, product_price, product_sugar_taxed) VALUES

-- Main courses
('Sandwich', 1, 'Fresh vegetables in a whole wheat bread', 3.50, 0),
('Cheese Sandwich', 1, 'Classic cheese sandwich', 4.00, 0),
('Egg Salad Sandwich', 1, 'Creamy egg salad with lettuce and tomato', 4.00, 0),
('Falafel Sandwich', 1, 'Spiced chickpea patties with tahini sauce', 4.50, 0),
('Grilled Veggie Sanwich', 1, 'Grilled seasonal vegetables in a wrap', 4.00, 0),
('Portobello Mushroom Sandwich', 1, 'Marinated portobello mushroom sandwich', 4.50, 0),
('Grilled Chicken Sandwich', 1, 'Grilled chicken breast with lettuce and mayo', 5.00, 0),
('Turkey Sandwich', 1, 'Sliced turkey with cranberry sauce and stuffing', 5.50, 0),
('Ham and Cheese Sandwich', 1, 'Classic ham and cheese sandwich', 5.50, 0),
('Hummus Wrap', 1, 'Creamy hummus with fresh veggies in a wrap', 4.00, 0),
('Grilled Veggie Hummus Wrap', 1, 'Grilled vegetables with hummus in a wrap', 4.50, 0),
('Greek Wrap', 1, 'Mediterranean-style wrap with feta and olives', 5.00, 0),
('Falafel Wrap', 1, 'Crispy falafel balls with tahini sauce in a wrap', 4.50, 0),
('Vegan Chicken Wrap', 1, 'Plant-based chicken strips with vegan mayo', 5.00, 0),
('Tofu Wrap', 1, 'Marinated tofu with fresh veggies in a wrap', 5.50, 0),
('Chicken Caesar Wrap', 1, 'Grilled chicken Caesar salad in a wrap', 5.50, 0),
('Turkey Club Wrap', 1, 'Turkey, bacon, lettuce, tomato, and mayo', 6.00, 0),
('Buffalo Chicken Wrap', 1, 'Spicy buffalo chicken with blue cheese dressing', 6.50, 0),
('Pesto Pasta', 1, 'Pasta tossed in basil pesto sauce', 6.00, 0),
('Primavera Pasta', 1, 'Mixed vegetables in a light tomato sauce', 6.50, 0),
('Mushroom Alfredo Pasta', 1, 'Creamy alfredo pasta with mushrooms', 7.00, 0),
('Vegan Alfredo Pasta', 1, 'Creamy vegan alfredo pasta with garlic', 7.00, 0),
('Spaghetti Aglio e Olio', 1, 'Spaghetti with garlic and olive oil', 6.50, 0),
('Pumpkin Ravioli', 1, 'Homemade pumpkin-filled ravioli in sage butter', 7.50, 0),
('Chicken Alfredo Pasta', 1, 'Grilled chicken in creamy alfredo sauce', 7.50, 0),
('Spaghetti Bolognese', 1, 'Classic spaghetti with meat sauce', 8.00, 0),
('Shrimp Scampi Pasta', 1, 'Garlic butter shrimp over angel hair pasta', 8.50, 0),
('Greek Salad', 1, 'Traditional Greek salad with feta and olives', 5.00, 0),
('Caprese Salad', 1, 'Tomato, mozzarella, and basil salad', 5.50, 0),
('Caesar Salad', 1, 'Classic Caesar salad with croutons and parmesan', 6.00, 0),
('Quinoa Salad', 1, 'Quinoa with mixed vegetables and vinaigrette', 6.00, 0),
('Mixed Bean Salad', 1, 'Assorted beans with veggies and herbs', 5.50, 0),
('Kale Salad', 1, 'Kale with avocado, nuts, and citrus dressing', 6.50, 0),
('Grilled Chicken Salad', 1, 'Grilled chicken breast over mixed greens', 7.00, 0),
('Steak Salad', 1, 'Sliced steak with roasted vegetables and balsamic', 8.00, 0),
('Cobb Salad', 1, 'Classic Cobb salad with chicken, bacon, and egg', 8.50, 0),
-- Snacks
('Apple', 2, 'Crisp and juicy apple', 1.00, 0),
('Banana', 2, 'Naturally sweet banana', 1.00, 0),
('Orange', 2, 'Vitamin C-rich orange', 1.00, 0),
('Grapes', 2, 'Sweet and refreshing grapes', 1.50, 0),
('Granola Bar', 2, 'Nutty granola bar', 1.50, 1),
('Chocolate Chip Cereal Bar', 2, 'Classic chocolate chip bar', 1.50, 1),
('Nutty Crunch Cereal Bar', 2, 'Crunchy bar with nuts and dried fruits', 2.00, 1),
('Potato Crisps', 2, 'Classic salted potato crisps', 1.00, 0),
('Tortilla Crisps', 2, 'Crispy tortilla crisps', 1.50, 0),
('Popcorn', 2, 'Light and fluffy popcorn', 1.50, 0),
('Chocolate Bar', 2, 'Rich and creamy chocolate bar', 1.50, 1),
('Gummy Bears', 2, 'Chewy and fruity gummy bears', 1.00, 1),
('Trail Mix', 2, 'Mixed nuts, seeds, and dried fruits', 2.00, 1),
-- Drinks
('Water', 3, 'Plain water, hydrating and refreshing', 0.80, 0),
('Coke', 3, 'Classic Coca-Cola', 1.50, 1),
('Sprite', 3, 'Refreshing lemon-lime soda', 1.50, 1),
('Fanta', 3, 'Fruity orange soda', 1.50, 1),
('Mountain Dew', 3, 'Citrus-flavored carbonated drink', 1.50, 1),
('Orange Juice', 3, 'Freshly squeezed orange juice', 2.00, 1),
('Apple Juice', 3, 'Crisp apple juice', 2.00, 1),
('Pineapple Juice', 3, 'Tropical pineapple juice', 2.50, 1),
('Red Bull', 3, 'Gives you wings!', 2.50, 1),
('Monster', 3, 'Unleash the beast', 2.50, 1),
('Rockstar', 3, 'Party like a rockstar', 2.50, 1);

"""


pop_inventory_table = """
INSERT INTO Inventory (product_id, quantity, created_at) VALUES

-- Drink category
(50, 10, '2024-04-18 12:00:00'),
(51, 20, '2024-04-18 12:15:00'),
(52, 15, '2024-04-18 12:30:00'),
(53, 18, '2024-04-18 12:45:00'),
(54, 22, '2024-04-18 13:00:00'),
(55, 8, '2024-04-18 13:15:00'),
(56, 10, '2024-04-18 13:30:00'),
(57, 12, '2024-04-18 13:45:00'),
(58, 25, '2024-04-18 14:00:00'),
(59, 30, '2024-04-18 14:15:00'),
(60, 18, '2024-04-18 14:30:00'),

-- Main category
(1, 15, '2024-04-18 14:45:00'),
(2, 20, '2024-04-18 15:00:00'),
(3, 10, '2024-04-18 15:15:00'),
(4, 15, '2024-04-18 15:30:00'),
(5, 10, '2024-04-18 15:45:00'),
(6, 12, '2024-04-18 16:00:00'),
(7, 25, '2024-04-18 16:15:00'),
(8, 20, '2024-04-18 16:30:00'),
(9, 18, '2024-04-18 16:45:00'),
(10, 15, '2024-04-18 17:00:00'),
(11, 10, '2024-04-18 17:15:00'),
(12, 12, '2024-04-18 17:30:00'),
(13, 25, '2024-04-18 17:45:00'),
(14, 20, '2024-04-18 18:00:00'),
(15, 18, '2024-04-18 18:15:00'),
(16, 15, '2024-04-18 18:30:00'),
(17, 20, '2024-04-18 18:45:00'),
(18, 10, '2024-04-18 19:00:00'),
(19, 15, '2024-04-18 19:15:00'),
(20, 12, '2024-04-18 19:30:00'),
(21, 25, '2024-04-18 19:45:00'),
(22, 20, '2024-04-18 20:00:00'),
(23, 18, '2024-04-18 20:15:00'),
(24, 15, '2024-04-18 20:30:00'),
(25, 20, '2024-04-18 20:45:00'),
(26, 10, '2024-04-18 21:00:00'),
(27, 15, '2024-04-18 21:15:00'),
(28, 12, '2024-04-18 21:30:00'),
(29, 25, '2024-04-18 21:45:00'),
(30, 20, '2024-04-18 22:00:00'),
(31, 18, '2024-04-18 22:15:00'),
(32, 15, '2024-04-18 22:30:00'),
(33, 20, '2024-04-18 22:45:00'),
(34, 10, '2024-04-18 23:00:00'),
(35, 15, '2024-04-18 23:15:00'),
(36, 12, '2024-04-18 23:30:00'),


-- Snack category
(37, 10, '2024-04-18 22:15:00'),
(38, 15, '2024-04-18 22:30:00'),
(39, 12, '2024-04-18 22:45:00'),
(40, 20, '2024-04-18 23:00:00'),
(41, 10, '2024-04-18 23:15:00'),
(42, 15, '2024-04-18 23:30:00'),
(43, 12, '2024-04-18 23:45:00'),
(44, 20, '2024-04-19 00:00:00'),
(45, 10, '2024-04-19 00:15:00'),
(46, 15, '2024-04-19 00:30:00'),
(47, 12, '2024-04-19 00:45:00'),
(48, 20, '2024-04-19 01:00:00'),
(49, 15, '2024-04-19 01:15:00')
"""
 

pop_subcategories_table = """
INSERT INTO Subcategories (subcategory_name, created_at) VALUES
('Fizzy',  '2024-04-19 01:15:00'),
('Fresh Juice', '2024-04-19 01:15:00'),
('Energy Drink', '2024-04-19 01:15:00'),
('Sandwich', '2024-04-19 01:15:00'),
('Wrap',  '2024-04-19 01:15:00'),
('Pasta', '2024-04-19 01:15:00'),
('Salad',  '2024-04-19 01:15:00'),
('Fruits', '2024-04-19 01:15:00'),
('Cereal Bars', '2024-04-19 01:15:00'),
('Crisps','2024-04-19 01:15:00'),
('Sweets',  '2024-04-19 01:15:00'),
('Vegetarian', '2024-04-19 01:15:00'),
('Non Vegetarian','2024-04-19 01:15:00'),
('Vegan',  '2024-04-19 01:15:00');
"""


pop_product_subcategories_table = """
INSERT INTO ProductSubcategories (product_id, subcategory_id) VALUES

-- Drinks 
(51, 1),
(52, 1),
(53, 1),
(54, 1),
(55, 2),
(56, 2),
(57, 2),
(58, 3),
(59, 3),
(60, 3),

-- Sandwiches
(1, 4),
(2, 4),
(3, 4),
(4, 4),
(5, 4),
(6, 4),
(7, 4),
(8, 4),
(9, 4),

-- Wraps
(10, 5),
(11, 5),
(12, 5),
(13, 5),
(14, 5),
(15, 5),
(16, 5),
(17, 5),
(18, 5),

-- Pasta
(19, 6),
(20, 6),
(21, 6),
(22, 6),
(23, 6),
(24, 6),
(25, 6),
(26, 6),
(27, 6),

-- Salads
(28, 7),
(29, 7),
(30, 7),
(31, 7),
(32, 7),
(33, 7),
(34, 7),
(35, 7),
(36, 7),

-- Fruits
(37, 8),
(38, 8),
(39, 8),
(40, 8),

-- Snacks
(41, 9),
(42, 9),
(43, 9),
(44, 10),
(45, 10),
(46, 10),
(47, 11),
(48, 11),
(49, 11),

-- Veg
(1, 12),
(2, 12),
(3, 12),
(10, 12),
(11, 12),
(12, 12),
(19, 12),
(20, 12),
(21, 12),
(28, 12),
(29, 12),
(30, 12),


-- Non Veg
(7,13),
(8, 13),
(9, 13),
(16, 13),
(17, 13),
(18, 13),
(25, 13),
(26, 13),
(27, 13),
(34, 13),
(35, 13),
(36, 13),

-- Vegan

(4, 14),
(5, 14),
(6, 14),
(13, 14),
(14, 14),
(15, 14),
(22, 14),
(23, 14),
(24, 14),
(31, 14),
(32, 14),
(33, 14)


"""


pop_business_rates_table = """
INSERT INTO BusinessRates (business_id, tax_rate, sugar_tax_rate, business_discount_rate)
VALUES
(1, 20.00, 5.00, 15.00),
(2, 20.00, 5.00, 16.00),
(3, 20.00, 5.00, 17.00),
(4, 20.00, 5.00, 18.00),
(5, 20.00, 5.00, 19.00);
"""

pop_product_type_subcategories_table = """
insert into ProductTypeSubcategories (product_type_id, subcategory_id, note) values
(1, 4, 'Sandwich'),
(1, 5, 'Wrap'),
(1, 6, 'Pasta'),
(1, 7, 'Salad'),
(2, 8, 'Fruits'),
(2, 9, 'Cereal Bars'),
(2, 10, 'Crisps'),
(2, 11, 'Sweets'),
(3, 1, 'Fizzy'),
(3, 2, 'Fresh Juice'),
(3, 3, 'Energy Drink');
"""