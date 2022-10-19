
import d_data_read as book

#  Takes formatted data and outputs the entire table to tabulated format
# =======================================================================


def show_all(data):
    table = book.data_read(data)
    data1 = []
    temp = []
    for item in table:
        for value in item.values():
            temp.append(value)
        data1.append(temp)
        temp = []
    return data1


print(show_all('phonebook.csv'))
# ===================== DELETE LATER ====================================


# table = [['', '', '', ''],
#          ['', '', '', ''],
#          ['', '', '', ''], ]

# header1 = ['ID', 'SURNAME', 'NAME', 'PHONE', 'DESCRIPTION']


# print(tabulate(table, headers=header1, tablefmt='fancy_grid', showindex='always'))
