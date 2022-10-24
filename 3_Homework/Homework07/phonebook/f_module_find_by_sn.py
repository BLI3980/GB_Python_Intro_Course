import d_data_read as read


#  Searches  for all available persons by search surname.
# =======================================================================

def find_by_surname(data: list) -> list:
    book = read.data_read(data)
    surname_list = []
    temp = []
    surname = input('\nEnter surname: ')
    for person in book:
        if person['Surname'] == surname:  
            for value in person.values():
                temp.append(value)
            surname_list.append(temp)
            temp = []
    return surname_list

