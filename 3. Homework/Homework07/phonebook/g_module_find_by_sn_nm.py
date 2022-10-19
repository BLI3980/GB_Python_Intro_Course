import d_data_read as read


def find_by_surname_name(data: list) -> list:
    book = read.data_read(data)
    surname_list = []
    temp = []
    surname = input('Enter surname: ')
    firstname = input('Enter firstname: ')
    for person in book:
        if person['Surname'] == surname and person['Name'] == firstname:
            for value in person.values():
                temp.append(value)
            surname_list.append(temp)
            temp = []
    return surname_list


# print(find_by_surname_name('phonebook.csv'))
