# import csv

# =============================================================================

# def get_new_employee_details() -> list:
#     new = {}
#     new['id'] = input('\nAssign an id to new employee: ')
#     new['surname'] = input('Enter the surname of new employee: ')
#     new['name'] = input('Enter the name of new employee: ')
#     new['last_name'] = input('Enter the last name of new employee: ')
#     new['position'] = input('Enter the position of new employee: ')
#     new['phone_number'] = input('Enter the phone number of new employee ')
#     new['salary'] = input('Enter the salary of new employee: ')
#     return (new)


# new_employee = get_new_employee_details()
# print()
# print(new_employee)
# print()


# def add_employee(new_employee: dict) -> list:
#     # new_person = new_employee
#     add = []
#     # add.append(input('\nEnter a surname: '))
#     # add.append(input('Enter a first name: '))
#     # add.append(input('Enter a phone number: '))
#     # add.append(input('Enter a description: '))
#     add.append(new_employee)
#     return add
#     with open(read.phonebook(), 'a', encoding='utf-8') as book:
#         for item in new_person:
#             book.write('\n')
#             for pos in range(len(item)-1):
#                 book.write(item[pos] + ',')
#             book.write(item[len(item)-1])
#     return new_person

# =============================================================================

# table = '3_Homework\Homework08\DB\database.csv'


# def read_csv(table: str) -> list:
#     employees = []
#     # table = '3_Homework\Homework08\DB\database.csv'
#     fields = ['id', 'surname', 'first_name', 'last name',
#               'position', 'phone_number', 'salary']
#     with open(table, 'r', encoding='utf-8') as book:
#         for line in book:
#             record = dict(zip(fields, line.strip().split(',')))
#             employees.append(record)
#     return employees


# print()
# original_database = read_csv(table)
# print(original_database)
# print()

# updated_database = original_database.append(new_employee)
# print(original_database)
# print(updated_database)

# =============================================================================

# def write_csv(database: list, employee: list) -> list:
#     with open(database, 'w', encoding='utf-8', newline='') as output:
#         csv_writer = csv.writer(output)
#         for row in employee:
#             csv_writer.writerow(row.values())


# # database = '3_Homework\Homework08\DB\database.csv'
# =============================================================================


# def get_change_values(id: str) -> dict:
#     fields = ['surname', 'first_name', 'last name',
#               'position', 'phone_number', 'salary']
#     new_values = {'id': id}
#     for item in fields:
#         answer = input(f'Do you want to change "{item}" (Y/N)?: ')
#         if answer.lower() == 'y':
#             new_values[item] = input(f'Enter the new value for "{item}": ')
#             print(new_values[item])
#         # if answer == 1:
#         #     # fields[item] == input(f'Enter the new value for "{item}":')
#         #     print(fields[item])
#     return new_values


# print(get_change_values(235))
# =============================================================================


def get_search_id() -> str:
    return input('Enter id of employee to edit or delete: ')


table = '3_Homework\Homework08\DB\database.csv'


def read_csv(table: str) -> list:
    employees = []
    fields = ['id', 'surname', 'first_name', 'last name',
              'position', 'phone_number', 'salary']
    with open(table, 'r', encoding='utf-8') as book:
        for line in book:
            record = dict(zip(fields, line.strip().split(',')))
            employees.append(record)
    return employees


def find_employee_by_id(employees: list, id: str) -> list:
    for employee in employees:
        if employee['id'] == id:
            return employee


def del_employee_by_id(employee: dict, id: str) -> list:
    for employee in range(len(database)):
        # print(database[employee])
        for (k, v) in database[employee].items():
            if k == 'id' and v == id:
                del database[employee]
                # print(database)


id = get_search_id()

print(find_employee_by_id(read_csv(table), id))
