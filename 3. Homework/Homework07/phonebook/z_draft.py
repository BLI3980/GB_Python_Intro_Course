# data = [['', '', '', ''],
#         ['', '', '', ''],
#         ['', '', '', ''], ]

import a_data_read as data
book = data.read_data('phonebook.csv')
data1 = []
temp = []
for item in book:
    for value in item.values():
        temp.append(value)
    data1.append(temp)
    temp = []

print(data1)
