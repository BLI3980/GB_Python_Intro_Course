import d_data_read as read


#  Allows to add new person details to the phone book.
# =======================================================================

def add_person() -> list:
    add = []
    new_person = []
    add.append(input('\nEnter a surname: '))
    add.append(input('Enter a first name: '))
    add.append(input('Enter a phone number: '))
    add.append(input('Enter a description: '))
    new_person.append(add)
    with open(read.phonebook(), 'a', encoding='utf-8') as book:
        for item in new_person:
            book.write('\n')
            for pos in range(len(item)-1):
                book.write(item[pos] + ',')
            book.write(item[len(item)-1])
    return new_person


