from datetime import datetime

class BusinessUserController:
    def __init__(self, app, business_user_service, view=None):
        self.business_user_service = business_user_service
        self.view = view    
        self.app = app
        self.selection = {"Main": None, "Snack":None, 'Drink':None, 'Date':None}
        self.selection = {'Main': 10, 'Snack': 41, 'Drink': 56, 'Date': None}
        self.parsed_selection = {"Main": None, "Snack":None, 'Drink':None, }



    def get_subcategory_names(self, product_type_id):
        result = self.business_user_service.get_subcategory_names(product_type_id)
        result = {item[0]:item[1] for item in result}
        print("Result", result)
        return result  
    
    def get_values_based_on_subcategory(self, subcategory_name):
        print(subcategory_name)
        result = self.business_user_service.get_values_based_on_subcategory(subcategory_name)
        result = {item[0]:item[1] for item in result}
        return result
    
    def get_product_by_subcategory(self, subcategory_id):
        result = self.business_user_service.get_product_by_subcategory(subcategory_id)
        result = {item[0]:item[1] for item in result}
        
        return result
    
    def get_subcatergory_dieatary_restrictions(self):
        result = {'Veg': 12, 'Non-Veg': 13, 'Vegan': 14}
        return result
    
    def logout(self):
        self.app.logged_in_user = None
        self.app.transition_to(self.app.states['login'])


    def get_product_selection_details(self):

        selection = self.selection
        for key, value in self.selection.items():

            product_id, product_name, product_type_id, product_description, product_price =\
            self.business_user_service.get_product_details(value)[0]

            self.parsed_selection[key] = {"product_id": product_id,
                                           "product_name": product_name, 
                                           "product_type_id": product_type_id,
                                           "product_description": product_description,
                                           "product_price": product_price}


    def get_employee_details(self, user_id):
        return self.business_user_service.get_employee_details(user_id)
    
    def get_business_details(self, business_id):
        return self.business_user_service.get_business_details(business_id)
    
    


    def create_order(self):

        print("*"*50)
        try: 
            self.get_product_selection_details()
            print(self.get_employee_details(int(self.app.logged_in_user)))
            user_id,employee_id, business_id = self.get_employee_details(self.app.logged_in_user)[0]

            order_data = {'user_id': user_id, 'employee_id': employee_id, 'business_id': business_id, 'order_date': self.convert_date_format(self.selection['Date'], True) }

            order_id = self.business_user_service.create_order(order_data)

            for key, value in self.parsed_selection.items():

                if key == 'Date':
                    continue

                order_details_data = {'order_id': order_id, 'product_id': value['product_id'], 'product_type_id':value['product_type_id']}
                self.business_user_service.create_order_details(order_details_data)
                
            print("*"*50)
            return True
        except Exception as e:
            print(e)
            return False
        


    def convert_date_format(self,date_str, sql):
        if sql:
            return datetime.strptime(date_str, '%d/%m/%y').strftime('%Y-%m-%d')
        else:
            return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d/%m/%y')




    
