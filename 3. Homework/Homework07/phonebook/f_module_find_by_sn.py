import d_data_read as read


def find_by_surname(data: list) -> list:
    book = read.data_read(data)
    surname_list = []
    temp = []
    surname = input('Enter surname: ')
    for person in book:
        if person['Surname'] == surname:  
            for value in person.values():
                temp.append(value)
            surname_list.append(temp)
            temp = []
    return surname_list


# print(find_by_surname('phonebook.csv'))
