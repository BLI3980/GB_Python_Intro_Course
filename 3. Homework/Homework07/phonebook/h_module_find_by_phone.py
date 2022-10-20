import d_data_read as read


#  Searches for person's details by his phone number.
# =======================================================================

def find_by_phone(data: list) -> list:
    book = read.data_read(data)
    by_phone = []
    temp = []
    phone = input('\nEnter the phone number: ')
    for person in book:
        if person['Phone'] == phone:
            for value in person.values():
                temp.append(value)
            by_phone.append(temp)
            temp = []
    if by_phone != []:
        return by_phone
    else:
        print('\nNo such phone number in the phonebook,')
        print('as you can see below.')


