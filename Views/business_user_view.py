from tkinter import *
from tkinter import ttk
from Views.base_view import BaseView
from datetime import datetime, timedelta

class BusinessUserView(BaseView):
    def __init__(self, window, controller):
        super().__init__(window)
        self.controller = controller
        self.menu_frame()
        self.window.geometry(self.controller.app.screen_size)
        self.window.title("Lunch App - Business User")




# Framse for Creating Order
    def menu_frame(self):
        self.clear_window()

        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Welcome Business User", 0, 1, 10, 3, 'nsew')
        self.view_orders_button = self.create_button(frame, "View Orders", None, 'disabled', 1, 1, 10)
        self.view_products_button = self.create_button(frame, "Create Order", self.create_order_main_frame, 'normal', 1, 2, 10)
        self.view_customers_button = self.create_button(frame, "Modify Order", None, 'disabled', 1, 3, 10)
        self.logout_button = self.create_button(frame, "Logout", self.controller.logout, 'normal', 2, 2, 10)


    def create_order_main_frame(self):
        self.window.geometry(self.controller.app.screen_size)

        self.clear_window()
        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Select Main", 0, 1, 10, 2, 'nsew')

        self.dropdown_1_dict = self.controller.get_subcategory_names('1')
        self.dropdown_1 = self.create_dropdown(frame, 'readonly', 1, 1, 2, 10, lambda event: self.on_selection_dropdown_1(event, main=True),
                                               values = self.format_dropdown_values(self.dropdown_1_dict))
        
        self.dropdown_2 = self.create_dropdown(frame, 'disabled', 2, 1, 2, 10, self.on_selection_dropdown_2)
        self.dropdown_3 = self.create_dropdown(frame, 'disabled', 3, 1, 2, 10, self.on_selection_final_dropdown)
        self.back_button = self.create_button(frame, "Back", self.menu_frame, 'normal', 4, 1, 10)
        self.submit_button = self.create_button(frame, "Submit", lambda: self.submit_button_clicked('Main'), 'disabled', 4, 2, 10)
        self.menu_button = self.create_button(frame, "Menu", self.menu_frame, 'normal', 5, 1, 10, 2)



    def create_order_snack_frame(self):
        self.window.geometry(self.controller.app.screen_size)

        self.clear_window()
        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Select Snack", 0, 1, 10, 2, 'nsew')
        self.dropdown_1_dict = self.controller.get_subcategory_names('2')
        self.dropdown_1 = self.create_dropdown(frame, 'readonly', 1, 1, 2, 10, lambda event: self.on_selection_dropdown_1(event, main=False),
                                               values = self.format_dropdown_values(self.dropdown_1_dict))
        self.dropdown_2 = self.create_dropdown(frame, 'disabled', 2, 1, 2, 10, self.on_selection_final_dropdown)
        self.back_button = self.create_button(frame, "Back", self.create_order_main_frame, 'normal', 3, 1, 10)
        self.submit_button = self.create_button(frame, "Submit", lambda: self.submit_button_clicked('Snack'), 'disabled', 3, 2, 10)
        self.menu_button = self.create_button(frame, "Menu", self.menu_frame, 'normal', 4, 1, 10, 2)


    def create_order_drink_frame(self):
        self.window.geometry(self.controller.app.screen_size)

        self.clear_window()
        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Select Drink", 0, 1, 10, 2, 'nsew')
        self.dropdown_1_dict = self.controller.get_subcategory_names('3')
        self.dropdown_1 = self.create_dropdown(frame, 'readonly', 1, 1, 2, 10, lambda event: self.on_selection_dropdown_1(event, main=False),
                                               values= self.format_dropdown_values(self.dropdown_1_dict))
        self.dropdown_2 = self.create_dropdown(frame, 'disabled', 2, 1, 2, 10, self.on_selection_final_dropdown)
        self.back_button = self.create_button(frame, "Back", self.create_order_snack_frame, 'normal', 3, 1, 10)
        self.submit_button = self.create_button(frame, "Submit", lambda: self.submit_button_clicked('Drink'), 'disabled', 3, 2, 10)
        self.menu_button = self.create_button(frame, "Menu", self.menu_frame, 'normal', 4, 1, 10, 2)


    def create_order_select_date_frame(self):
        self.window.geometry(self.controller.app.screen_size)

        self.clear_window()
        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Select Order Date", 0, 1, 10, 2, 'nsew')

        dates = [(datetime.now() + timedelta(days=i)).strftime('%d/%m/%y') for i in range(14)]      

        self.dropdown_date = self.create_dropdown(frame, 'readonly', 1, 1, 2, 10, 
                                                    binding_func= lambda event: self.on_selection_final_dropdown(event),
                                                    values=dates,)


        self.back_button = self.create_button(frame, "Back", self.create_order_drink_frame, 'normal', 2, 1, 10)
        self.submit_button = self.create_button(frame, "Submit", lambda : self.submit_button_clicked("Date"), 'disabled', 2, 2, 10)
        self.menu_button = self.create_button(frame, "Menu", self.menu_frame, 'normal', 3, 1, 10, 2)


# Action on user selection

    
    def on_selection_dropdown_1(self, event, main=False):
        self.on_selection_clear(event)
        self.dropdown_2.set('')
        self.dropdown_2['state'] = 'readonly'
        if main:
            self.dropdown_3.set('')
            self.dropdown_3['state'] = 'disabled'
            self.dropdown_2_dict = self.controller.get_subcatergory_dieatary_restrictions()
            
            
        else:
            self.dropdown_2_dict = self.controller.get_product_by_subcategory(self.dropdown_1_dict[self.dropdown_1.get()])

        self.dropdown_2['values'] = self.format_dropdown_values(self.dropdown_2_dict)
        self.submit_button['state'] = 'disabled'

        
        self.dropdown_2['state'] = 'readonly'


    def on_selection_dropdown_2(self, event):

        self.on_selection_clear(event)
        entry_1 = self.dropdown_1_dict[self.dropdown_1.get()]
        entry_2 = self.dropdown_2_dict[self.dropdown_2.get()]

        self.dropdown_3_dict = self.controller.get_values_based_on_subcategory([entry_1, entry_2])
        
        self.dropdown_3.set('')
        self.dropdown_3['state'] = 'readonly'
        self.dropdown_3['values'] = self.format_dropdown_values(self.dropdown_3_dict)

        self.submit_button['state'] = 'disabled'

    def on_selection_final_dropdown(self, event):
        self.on_selection_clear(event)
        self.submit_button['state'] = 'normal'

    def submit_button_clicked(self, product_type):

        print("Submit button clicked")
        if product_type == 'Main':
            self.controller.selection[product_type] = self.dropdown_3_dict[self.dropdown_3.get()]
            self.create_order_snack_frame()
        elif product_type == 'Snack':   
            self.controller.selection[product_type] = self.dropdown_2_dict[self.dropdown_2.get()]
            self.create_order_drink_frame()
        elif product_type == 'Drink':
            self.controller.selection[product_type] = self.dropdown_2_dict[self.dropdown_2.get()]
            self.create_order_select_date_frame()
        elif product_type == 'Date':
            self.controller.selection[product_type] = self.dropdown_date.get()
            

            self.controller.get_product_selection_details()
            self.confirm_order_frame()

    

    def confirm_order_frame(self):
        self.window.geometry("500x500")
        self.clear_window()
        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Confirm Order", 0, 1, 10, 2, 'nsew', font=('Helvetica', 15, 'bold'))


        main_frame = Frame(frame, bg='lightgrey')
        main_frame.place(relx=0.5, rely=0.5, anchor='center')

        main_frame.grid(row=5, column=1, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.create_label(main_frame, "Main", 0, 0, 10, 2, 'w', font =('Helvetica', 14, 'underline'),bg='lightgrey')
        self.create_label(main_frame, "Product Name:", 1, 0, 10, 1, 'w',bg='lightgrey')
        self.create_label(main_frame, self.controller.parsed_selection['Main']['product_name'], 1, 1, 10, 1, 'w',bg='lightgrey')
        self.create_label(main_frame, "Description:", 2, 0, 10, 2, 'w',bg='lightgrey')
        self.create_label(main_frame, self.controller.parsed_selection['Main']['product_description'], 3, 0, 10, 2, 'w',bg='lightgrey')


        snack_frame = Frame(frame, bg = 'lightgrey')
        snack_frame.place(relx=0.5, rely=0.5, anchor='center')

        snack_frame.grid(row=9, column=1, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.create_label(snack_frame, "Snack: ", 0, 0, 10, 2, 'w', font =('Helvetica', 14, 'underline'),bg='lightgrey')
        self.create_label(snack_frame, "Product Name:", 1, 0, 10, 1, 'w',bg='lightgrey')
        self.create_label(snack_frame, self.controller.parsed_selection['Snack']['product_name'], 1, 1, 10, 1, 'w',bg='lightgrey')
        self.create_label(snack_frame, "Description:", 2, 0, 10, 2, 'w',bg='lightgrey')
        self.create_label(snack_frame, self.controller.parsed_selection['Snack']['product_description'], 3, 0, 10, 2, 'w',bg='lightgrey')
            
        drink_frame = Frame(frame, bg='lightgrey')
        drink_frame.place(relx=0.5, rely=0.5, anchor='center')

        drink_frame.grid(row=13, column=1, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.create_label(drink_frame, "Drink: ", 0, 0, 10, 2, 'w', font =('Helvetica', 14, 'underline'),bg='lightgrey')
        self.create_label(drink_frame, "Product Name:", 1, 0, 10, 1, 'w',bg='lightgrey')
        self.create_label(drink_frame, self.controller.parsed_selection['Drink']['product_name'], 1, 1, 10, 1, 'w',bg='lightgrey')
        self.create_label(drink_frame, "Description:", 2, 0, 10, 2, 'w',bg='lightgrey')
        self.create_label(drink_frame, self.controller.parsed_selection['Drink']['product_description'], 3, 0, 10, 2, 'w',bg='lightgrey')
        

        date_frame = Frame(frame, bg='lightgrey')
        date_frame.place(relx=0.5, rely=0.5, anchor='center')

        date_frame.grid(row=17, column=1, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.create_label(date_frame, "Date: ", 0, 0, 10, 1, 'w', font =('Helvetica', 14, 'underline'),bg='lightgrey')
        self.create_label(date_frame, self.controller.selection['Date'], 0, 1, 10, 1, 'w',bg='lightgrey')

        
        self.back_button = self.create_button(frame, "Back", self.create_order_select_date_frame, 'normal', 18, 1, 10)
        self.submit_button = self.create_button(frame, "Submit", self.order_confirmation_frame, 'normal', 18, 2, 10)
        self.menu_button = self.create_button(frame, "Menu", self.menu_frame, 'normal', 19, 1, 10, 2, 'nsew')


    def order_confirmation_frame(self):
        self.window.geometry(self.controller.app.screen_size)


        result = self.controller.create_order()

        if result:
            text = "Order Created Successfully"
        else:
            text = "Order Creation Failed"


        self.window.geometry("500x200")
        self.clear_window()
        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = self.create_label(frame, "Order Confirmation", 0, 1, 10, 2, 'nsew')

        self.label = self.create_label(frame, text, 1, 1, 10, 2, 'nsew')

        if result:
            self.menu_button = self.create_button(frame, "Return to Menu", self.menu_frame, 'normal', 2, 1, 10, 2)
        else:
            self.back_button =  self.create_button(frame, "Back", self.confirm_order_frame, 'normal', 2, 1, 10)
            self.menu_button = self.create_button(frame, "Return to Menu", self.menu_frame, 'normal', 2, 2, 10, 1)

