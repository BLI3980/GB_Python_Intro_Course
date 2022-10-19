
import a_data_read as input

#  Takes formatted data and outputs the entire table to terminal


def show_all(data):
    book = input.read_data(data)
    data1 = []
    temp = []
    for item in book:
        for value in item.values():
            temp.append(value)
        data1.append(temp)
        temp = []
    return data1


# ===================== DELETE LATER ===========================
# show_all('phonebook.csv')

# table = [['', '', '', ''],
#          ['', '', '', ''],
#          ['', '', '', ''], ]

# header1 = ['ID', 'SURNAME', 'NAME', 'PHONE', 'DESCRIPTION']


# print(tabulate(table, headers=header1, tablefmt='fancy_grid', showindex='always'))
