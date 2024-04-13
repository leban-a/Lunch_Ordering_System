database = {
    "Drink": {
        'Water': {'price': 0.80, 'description': 'Plain water, hydrating and refreshing', 'Product': 'Drink', 'SugarTax': False},
        'Fizzy': {
            'Coke': {'price': 1.50, 'description': 'Classic Coca-Cola', 'Product': 'Drink', 'SugarTax': True},
            'Sprite': {'price': 1.50, 'description': 'Refreshing lemon-lime soda', 'Product': 'Drink', 'SugarTax': True},
            'Fanta': {'price': 1.50, 'description': 'Fruity orange soda', 'Product': 'Drink', 'SugarTax': True},
            'Mountain Dew': {'price': 1.50, 'description': 'Citrus-flavored carbonated drink', 'Product': 'Drink', 'SugarTax': True}
        },
        'Fresh Juice': {
            'Orange': {'price': 2.00, 'description': 'Freshly squeezed orange juice', 'Product': 'Drink', 'SugarTax': True},
            'Apple': {'price': 2.00, 'description': 'Crisp apple juice', 'Product': 'Drink', 'SugarTax': True},
            'Pineapple': {'price': 2.50, 'description': 'Tropical pineapple juice', 'Product': 'Drink', 'SugarTax': True}
        },
        'Energy Drink': {
            'Red Bull': {'price': 2.50, 'description': 'Gives you wings!', 'Product': 'Drink', 'SugarTax': True},
            'Monster': {'price': 2.50, 'description': 'Unleash the beast', 'Product': 'Drink', 'SugarTax': True},
            'Rockstar': {'price': 2.50, 'description': 'Party like a rockstar', 'Product': 'Drink', 'SugarTax': True}
        }
    },

    'Main': {
        'Sandwich': {
            'Veg': {
                'Vegetable': {'price': 3.50, 'description': 'Fresh vegetables in a whole wheat bread', 'Product': 'Main', 'SugarTax': False},
                'Cheese': {'price': 4.00, 'description': 'Classic cheese sandwich', 'Product': 'Main', 'SugarTax': False},
                'Egg Salad': {'price': 4.00, 'description': 'Creamy egg salad with lettuce and tomato', 'Product': 'Main', 'SugarTax': False}
            },
            'Vegan': {
                'Falafel': {'price': 4.50, 'description': 'Spiced chickpea patties with tahini sauce', 'Product': 'Main', 'SugarTax': False},
                'Grilled Veggie': {'price': 4.00, 'description': 'Grilled seasonal vegetables in a wrap', 'Product': 'Main', 'SugarTax': False},
                'Portobello Mushroom': {'price': 4.50, 'description': 'Marinated portobello mushroom sandwich', 'Product': 'Main', 'SugarTax': False}
            },
            'Meat': {
                'Chicken': {'price': 5.00, 'description': 'Grilled chicken breast with lettuce and mayo', 'Product': 'Main', 'SugarTax': False},
                'Turkey': {'price': 5.50, 'description': 'Sliced turkey with cranberry sauce and stuffing', 'Product': 'Main', 'SugarTax': False},
                'Ham and Cheese': {'price': 5.50, 'description': 'Classic ham and cheese sandwich', 'Product': 'Main', 'SugarTax': False}
            }
        },

        'Wrap': {
            'Veg': {
                'Hummus': {'price': 4.00, 'description': 'Creamy hummus with fresh veggies in a wrap', 'Product': 'Main', 'SugarTax': False},
                'Grilled Veggie': {'price': 4.50, 'description': 'Grilled vegetables with hummus in a wrap', 'Product': 'Main', 'SugarTax': False},
                'Greek Wrap': {'price': 5.00, 'description': 'Mediterranean-style wrap with feta and olives', 'Product': 'Main', 'SugarTax': False}
            },
            'Vegan': {
                'Falafel': {'price': 4.50, 'description': 'Crispy falafel balls with tahini sauce in a wrap', 'Product': 'Main', 'SugarTax': False},
                'Vegan Chicken': {'price': 5.00, 'description': 'Plant-based chicken strips with vegan mayo', 'Product': 'Main', 'SugarTax': False},
                'Tofu Wrap': {'price': 5.50, 'description': 'Marinated tofu with fresh veggies in a wrap', 'Product': 'Main', 'SugarTax': False}
            },
            'Meat': {
                'Chicken Caesar': {'price': 5.50, 'description': 'Grilled chicken Caesar salad in a wrap', 'Product': 'Main', 'SugarTax': False},
                'Turkey Club': {'price': 6.00, 'description': 'Turkey, bacon, lettuce, tomato, and mayo', 'Product': 'Main', 'SugarTax': False},
                'Buffalo Chicken': {'price': 6.50, 'description': 'Spicy buffalo chicken with blue cheese dressing', 'Product': 'Main', 'SugarTax': False}
            }
        },

        'Pasta': {
            'Veg': {
                'Pesto Pasta': {'price': 6.00, 'description': 'Pasta tossed in basil pesto sauce', 'Product': 'Main', 'SugarTax': False},
                'Primavera': {'price': 6.50, 'description': 'Mixed vegetables in a light tomato sauce', 'Product': 'Main', 'SugarTax': False},
                'Mushroom Alfredo': {'price': 7.00, 'description': 'Creamy alfredo pasta with mushrooms', 'Product': 'Main', 'SugarTax': False}
            },
            'Vegan': {
                'Vegan Alfredo': {'price': 7.00, 'description': 'Creamy vegan alfredo pasta with garlic', 'Product': 'Main', 'SugarTax': False},
                'Spaghetti Aglio e Olio': {'price': 6.50, 'description': 'Spaghetti with garlic and olive oil', 'Product': 'Main', 'SugarTax': False},
                'Pumpkin Ravioli': {'price': 7.50, 'description': 'Homemade pumpkin-filled ravioli in sage butter', 'Product': 'Main', 'SugarTax': False}
            },
            'Meat': {
                'Chicken Alfredo': {'price': 7.50, 'description': 'Grilled chicken in creamy alfredo sauce', 'Product': 'Main', 'SugarTax': False},
                'Spaghetti Bolognese': {'price': 8.00, 'description': 'Classic spaghetti with meat sauce', 'Product': 'Main', 'SugarTax': False},
                'Shrimp Scampi': {'price': 8.50, 'description': 'Garlic butter shrimp over angel hair pasta', 'Product': 'Main', 'SugarTax': False}
            }
        },

        'Salad': {
            'Veg': {
                'Greek Salad': {'price': 5.00, 'description': 'Traditional Greek salad with feta and olives', 'Product': 'Main', 'SugarTax': False},
                'Caprese Salad': {'price': 5.50, 'description': 'Tomato, mozzarella, and basil salad', 'Product': 'Main', 'SugarTax': False},
                'Caesar Salad': {'price': 6.00, 'description': 'Classic Caesar salad with croutons and parmesan', 'Product': 'Main', 'SugarTax': False}
            },
            'Vegan': {
                'Quinoa Salad': {'price': 6.00, 'description': 'Quinoa with mixed vegetables and vinaigrette', 'Product': 'Main', 'SugarTax': False},
                'Mixed Bean Salad': {'price': 5.50, 'description': 'Assorted beans with veggies and herbs', 'Product': 'Main', 'SugarTax': False},
                'Kale Salad': {'price': 6.50, 'description': 'Kale with avocado, nuts, and citrus dressing', 'Product': 'Main', 'SugarTax': False}
            },
            'Meat': {
                'Grilled Chicken Salad': {'price': 7.00, 'description': 'Grilled chicken breast over mixed greens', 'Product': 'Main', 'SugarTax': False},
                'Steak Salad': {'price': 8.00, 'description': 'Sliced steak with roasted vegetables and balsamic', 'Product': 'Main', 'SugarTax': False},
                'Cobb Salad': {'price': 8.50, 'description': 'Classic Cobb salad with chicken, bacon, and egg', 'Product': 'Main', 'SugarTax': False}
            }
        }
    },

    'Snack': {
        'Fruits': {
            'Apple': {'price': 1.00, 'description': 'Crisp and juicy apple', 'Product': 'Snack', 'SugarTax': False},
            'Banana': {'price': 1.00, 'description': 'Naturally sweet banana', 'Product': 'Snack', 'SugarTax': False},
            'Orange': {'price': 1.00, 'description': 'Vitamin C-rich orange', 'Product': 'Snack', 'SugarTax': False},
            'Grapes': {'price': 1.50, 'description': 'Sweet and refreshing grapes', 'Product': 'Snack', 'SugarTax': False}
        },
        'Cereal Bars': {
            'Granola': {'price': 1.50, 'description': 'Nutty granola bar', 'Product': 'Snack', 'SugarTax': True},
            'Chocolate Chip': {'price': 1.50, 'description': 'Classic chocolate chip bar', 'Product': 'Snack', 'SugarTax': True},
            'Nutty Crunch': {'price': 2.00, 'description': 'Crunchy bar with nuts and dried fruits', 'Product': 'Snack', 'SugarTax': True}
        },
        'Crisps': {
            'Potato crisps': {'price': 1.00, 'description': 'Classic salted potato crisps', 'Product': 'Snack', 'SugarTax': False},
            'Tortilla crisps': {'price': 1.50, 'description': 'Crispy tortilla crisps', 'Product': 'Snack', 'SugarTax': False},
            'Popcorn': {'price': 1.50, 'description': 'Light and fluffy popcorn', 'Product': 'Snack', 'SugarTax': False}
        },
        'Sweets': {
            'Chocolate Bar': {'price': 1.50, 'description': 'Rich and creamy chocolate bar', 'Product': 'Snack', 'SugarTax': True},
            'Gummy Bears': {'price': 1.00, 'description': 'Chewy and fruity gummy bears', 'Product': 'Snack', 'SugarTax': True},
            'Trail Mix': {'price': 2.00, 'description': 'Mixed nuts, seeds, and dried fruits', 'Product': 'Snack', 'SugarTax': True}
        }
    }
}


sugar_tax_rate = 0.05

def main():
    
    # Define the meal deal options
    meal_deal_options = ['Main','Snack','Drink']

    

    # Test 
    # meal_deal_product_keys  = [['Main', 'Sandwich', 'Veg', 'Cheese'], ['Snack', 'Fruits', 'Apple'], ['Drink', 'Fizzy', 'Coke']] 

    # Get the user selection for each meal deal option
    meal_deal_product_keys  = [get_selection(option) for option in meal_deal_options]

    # Get the prices of the selected products from the database
    meal_deal_product_prices = [get_database(product_keys, database)['price'] for product_keys in meal_deal_product_keys]

    # Calculate the total price of the meal deal
    meal_deal_price = sum(meal_deal_product_prices)

    # Find the discount (lowest price) among the selected products
    meal_deal_discount = sorted(meal_deal_product_prices)[0]

    # Calculate the sugar tax for the selected products
    sugar_tax = sum([get_database(product_keys, database).get("price") * sugar_tax_rate for product_keys in meal_deal_product_keys if get_database(product_keys, database).get("SugarTax")])

    # Calculate the total cost including sugar tax and discount
    total_cost = meal_deal_price + sugar_tax - meal_deal_discount


    print(f"You've choosen a {meal_deal_product_keys[0][-1]} {meal_deal_product_keys[0][1]} as your Main a {meal_deal_product_keys[1][-1]} as a snack and {meal_deal_product_keys[2][-1]} for a drink")
    print(f"Meal Deal Price £{meal_deal_price:.2f} \nMeal Deal Discount £{meal_deal_discount:.2f} \nSugarTax: £{sugar_tax:.2f} ")
    print(f"For a total of £{total_cost:.2f}")



# Function to display the available options for a given category and check if any products are listed
def step_through_database(keys, database):
    # Initialize the flag indicating if any products are listed to False
    product_listed = False 
    # Print a message prompting the user to select their choice for the current category
    print(f"\n\nPlease select your {keys[-1]}\n")
    # Iterate through each key in the database
    for key in database.keys():
        # Check if the current key represents a product
        if database[key].get("Product"):
            # Set the flag to True indicating that at least one product is listed
            product_listed = True
            # Print the details of the product including its price and description
            print(f"{key} £{database[key]['price']} \n{database[key]['description']}\n")        
        else:
            # Print the key if it does not represent a product
            print(key)
    # Return the flag indicating if any products are listed
    return product_listed

        
    


# Function to prompt the user for input and return their selection if it exists in the database
def get_input(database):
    # Loop indefinitely until a valid input is received
    while True:
        # Prompt the user for input
        user_input = input("\n> ")
        # Check if the user's input exists in the database
        if database.get(user_input):
            # Return the user's input
            return user_input

# Function to retrieve data from the database based on a list of keys
def get_database(keys, database):
    # Iterate through each key in the list
    for key in keys:
        # Update the database with the data corresponding to the current key
        database = database[key]
    # Return the final database after all keys are processed
    return database


# Function to recursively prompt the user to select an item from a given category
def get_selection(target):
    # Initialize the list of keys with the initial category
    keys = [target]
    # Retrieve the data for the initial category from the database
    working_database = get_database(keys, database)
    # Initialize the selection flag to False
    selection = False
    # Loop until a valid selection is made
    while not selection:
        # Display the available options for the current category and check if any products are listed
        product_listed = step_through_database(keys, working_database)
        # Prompt the user for input and get their selection
        user_input = get_input(working_database)
        # Append the user's selection to the keys list
        keys.append(user_input)
        # Update the working database with the data for the new category based on the user's selection
        working_database = get_database(keys, database)
        # Check if a valid product is selected
        if product_listed and working_database.get('Product', False):
            # Return the list of keys representing the chosen products
            return keys



        
if __name__ == '__main__':
    main()