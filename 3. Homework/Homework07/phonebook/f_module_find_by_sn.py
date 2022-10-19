import a_data_read as read

# Option 1: find by name and surname
def Format1(data):
    book = read.read_data(data)
    # print(book)
    surname = input('Enter surname: ')
    firstname = input('Enter firstname: ')
    for item in book:
        # print(item)
        for (key, value) in item.items():
            condition1 = (key == 'Surname' and value == surname)
            condition2 = (key == 'Name' and value ==
                          firstname and surname_found)
            if condition1:
                surname_found = True
            if condition2 and surname_found:
                print('Phone number: {}'.format(item['Phone']))


# Format1('phonebook.csv')

# =====================================================
# Format1({'up': '↑', 'left': '←', 'down': '↓', 'right': '→'})


# dictionary = {}

# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }

# print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left'])  # ←

# for k in dictionary.keys():
#     print(k)  # Print all keys

# for v in dictionary.values():
#     print(v)  # Print all values

# for v in dictionary:
#     print(v)  # Print all keys

# for v in dictionary:
#     print(dictionary[v])  # Print all values

# del dictionary['left']  # Delete and element

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# for (k, v) in dictionary.items():
#     print(k, v)
