import d_data_read as read


#  Searches for a unique person by search surname and first name.
# =======================================================================


def find_by_surname_name(data: list) -> list:
    book = read.data_read(data)
    surname_list = []
    temp = []
    surname = input('\nEnter surname: ')
    firstname = input('Enter first name: ')
    for person in book:
        if person['Surname'] == surname and person['Name'] == firstname:
            for value in person.values():
                temp.append(value)
            surname_list.append(temp)
            temp = []
    return surname_list


