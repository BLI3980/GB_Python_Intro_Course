from tabulate import tabulate

data = [['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''], ]

header1 = ['id', 'surname', 'name', 'phone', 'description']


print(tabulate(data, headers=header1, tablefmt='fancy_grid', showindex='always'))



