# data = [['', '', '', ''],
#         ['', '', '', ''],
#         ['', '', '', ''], ]

import a_data_read as data
book = data.read_data('phonebook.csv')
data = []
temp = []
for item in book:
    for value in item.values():
        temp.append(value)
        data.append(temp)
        temp = []

print(data)
