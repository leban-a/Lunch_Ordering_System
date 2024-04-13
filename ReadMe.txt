### Meal Deal

This codebase implements a meal deal calculator that allows users to create customized meal deals consisting of a main dish, a snack, and a drink. The meal deal options are predefined, and the user can choose from a variety of items available in each category.

#### Methods Used:

1. **main()**: This function serves as the main entry point for the meal deal calculator. It prompts the user to select items for each meal deal category, calculates the total cost of the meal deal including any applicable discounts and sugar tax, and then prints the details of the meal deal.

2. **step_through_database(keys, database)**: This function displays the available options for a given category from the database and checks if any products are listed. It iterates through each key in the database, prints the details of the products including their prices and descriptions, and returns a boolean indicating if any products are listed. A product is defined as listed when its displayed to the user at this stage the user can make thier final selection for a given category. 


3. **get_input(database)**: This function prompts the user for input and returns their selection if it exists in the provided database. It loops indefinitely until a valid input is received, checking if the input exists in the database before returning it.

4. **get_database(keys, database)**: This function retrieves data from the database based on a list of keys. It iterates through each key in the list, updating the database with the data corresponding to the current key, and returns the final database after all keys are processed.

5. **get_selection(target)**: This function recursively prompts the user to select an item from a given category until a valid selection is made. It initializes a list of keys with the initial category, retrieves the corresponding data from the database, and enters a loop until a valid selection is made. Within the loop, it displays the available options for the current category, prompts the user for input, and updates the keys list with the user's selection. After each iteration, it updates the working database with the new category data based on the user's input. If a valid product is selected, it returns the list of keys representing the chosen products.
