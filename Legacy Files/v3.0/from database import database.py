from database import database

#Final values stored in dictionary.
global values_to_retrieve, values_retrieved

values_retrieved = []
selection_approved = False

values_to_retrieve = {
    "Movie": None,
    "City": None,
    "Theater": None,
    "Time": None,
    "Screen": None
}

tickets = {"Kids": None, "Adults": None}
tickets_cost = {'Kids':None, 'Adults':None}


def get_screen(database):

  for item, value in values_to_retrieve:
    database = database[item][value]

  return database


def get_database_view(database):

  for item, value in values_to_retrieve.items():

    if value is None:
      return database[item]
    else:
      database = database[item][value]


def get_working_item():

  for item, value in values_to_retrieve.items():
    if value is None:
      return item

  return None


def extract_database_view(database_view):

  if isinstance(database_view, list):
    return database_view
  else:
    return [key for key in database_view]


def get_input(database, working_item):

  print(f"\n\n--------------{working_item}------------\n\n")
  for i in database:
    print(f"\t{i}")
  print("\n-----------------------------------")
  while True:
    user_input = input(f"\n\nPlease select a {working_item}:  ")

    if user_input in database:
      return user_input
    elif user_input == 'back' and values_retrieved:
      values_to_retrieve[values_retrieved.pop()] = None
      return user_input
    elif user_input == 'exit':
      return user_input


def get_screening_selection(database):

  while len(values_retrieved) != 5:

    working_item = get_working_item()
    working_database = get_database_view(database)
    user_input = get_input(extract_database_view(working_database),
                           working_item)

    if user_input == 'exit':
      print('Exiting...')
      break
    elif user_input == 'back':
      continue
    else:
      values_to_retrieve[working_item] = user_input
      values_retrieved.append(working_item)


def calulate_ticket_prices(database):
  pass


def get_ticket_selection(database):

  print("How many Adult tickets would you like?")
  adult_tickets = input("> ")
  while True:
    adult_tickets = input('> ')
    if adult_tickets.isnumeric():
      tickets['Adults'] = adult_tickets
      break

  if database['Movie'][values_to_retrieve['Movie']]['Rating'] in [
      'U', 'PG', 'PG-13'
  ]:
    print("How many Kids tickets would you like?")

    while True:
      kids_tickets = input("> ")
      if kids_tickets.isnumeric():
        tickets['Kids'] = kids_tickets
        break

  kids_ticket_price = kids_tickets * database['Movie'] [values_to_retrieve['Movie']] ['Ticket_price']['Kids']

  tickets_cost['Kids']= kids_ticket_price

  adult_ticket_price = adult_tickets * database['Movie'][values_to_retrieve['Movie']]['Ticket_price'] ['Adults']


  
  tickets_cost['Adults'] = adult_ticket_price
  


def output_selection(output):

  if output == 'movie':

    print("\n---------- Movie - Selection - Details ----------\n\n")

    for item, value in values_to_retrieve.items():
      print(f"\t\t\t{item}: {value}\n")

    print("\n-----------------------------------------------\n")

    while True:
      user_input = input("Are you happy with your selectuion (y/n)?: ")
      if user_input == 'y':
        print("Thank you for your selection!")
        print("Please procees to ticket booking.")
        break
      elif user_input == 'n':
        print("Please select again.")
        values_to_retrieve = {
            "Movie": None,
            "City": None,
            "Theater": None,
            "Time": None,
            "Screen": None
        }
        values_retrieved = []
        get_screening_selection(database)

  if output == 'tickets':
    print("\n---------- Ticket - Selection - Details ----------\n\n")

    for key, value in tickets.items():

      if value is not None:
        print(f"\t\t\t{key}: {value}\n")
    print("\n-----------------------------------------------\n")

    while True:
      user_input = input("Are you happy with your selectuion (y/n)?: ")
      if user_input == 'y':
        print("Thank you for your selection!")
        break
      elif user_input == 'n':
        print("Please select again.")
        tickets = {"Kids": None, "Adults": None}
        get_ticket_selection(database)



  if output == 'final': 
    print(f"\n\n---------- Final - Selection - Details ----------\n\n")
    for item, value in values_to_retrieve.items():
      print(f"\t\t\t{item}: {value}\n")
      
    for key in tickets.keys():
      if tickets[key] is not None:
        print(f"\t\t\t{key}: {tickets[keys]} = £{tickets_cost[key]}")
    
    print(f"\t\t\tTotal = £{tickets_cost['Kids'] + tickets_cost['Adults']}")

    

    print("\n-----------------------------------------------\n")


  print("\t\t\tLooking forward to seeing you soon!")
    



def main():

  global values_retrieved, values_to_retrieve

  while True:
    get_screening_selection(database)
    output_selection('movie')

    get_ticket_selection(database)
    output_selection('tickets')

    

    output_selection('final')


if __name__ == "__main__":
  main()
