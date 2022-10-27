from pathlib import Path
import json
import csv
from view import (get_surname_name_to_search,
                  get_position_to_search, get_salary_range_to_search,
                  get_new_employee_details, get_search_id)


# Uploads DB file in csv extension and outputs it to the format we like.
# =======================================================================


# def read_csv(table: str) -> list:
#     employee = []
#     with open(table, 'r', encoding='utf-8') as fin:
#         csv_reader = csv.reader(fin)
#         for row in csv_reader:
#             temp = {}
#             temp["id"] = int(row[0])
#             temp["last_name"] = row[1]
#             temp["first_name"] = row[2]
#             temp["position"] = row[3]
#             temp["phone_number"] = row[4]
#             temp["salary"] = float(row[5])
#             employee.append(temp)
#     return employee


def read_csv(table: str) -> list:
    employees = []
    fields = ['id', 'surname', 'first_name', 'last name',
              'position', 'phone_number', 'salary']
    with open(table, 'r', encoding='utf-8') as book:
        for line in book:
            record = dict(zip(fields, line.strip().split(',')))
            employees.append(record)
    return employees


# print(read_csv(database(1)))
# print()
# print()

# Uploads DB file in json extension and outputs it to the format we like.
# =======================================================================


def read_json(database: list) -> list:
    employee = []
    with open(database, 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


# print(read_json(database(2)))

# Takes a DB chosen by user and transforms it into format for printing.
# =============================================================================

# def database(select: int) -> str:
#     if select == 1:
#         source = '3_Homework\Homework08\DB\database.csv'
#         database =
#     elif select == 2:
#         source = '3_Homework\Homework08\DB\database02.json'
#     return database


# print(database(2))

# Takes existing database in csv format re-writes it back to database file.
# =============================================================================


def write_csv(database: str, updates: list) -> list:
    with open(database, 'w', encoding='utf-8', newline='') as output:
        csv_writer = csv.writer(output)
        for row in updates:
            csv_writer.writerow(row.values())


# Takes existing database in json format re-writes it back to database file.
# =============================================================================


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


# Finds an employee by his last and first names.
# =============================================================================
def find_employee_by_surname_name(database: list) -> list:
    surname, first_name = get_surname_name_to_search()
    search_result = []
    for employee in database:
        if employee['surname'] == surname and\
                employee['first_name'] == first_name:
            search_result.append(employee)
    if search_result == []:
        print('\nThere is no such employee.\n')
    return search_result


# print(find_employee_by_last_first_names(
#     read_csv('3_Homework\Homework08\DB\database.csv')))

# Finds a list of employees by position.
# =============================================================================
def find_employees_by_position(database: list) -> list:
    position = get_position_to_search()
    search_result = []
    not_found = False
    for employee in database:
        if employee['position'] == position:
            search_result.append(employee)
    if search_result == []:
        print('\nThere is no such position in this organization.\n')
    return search_result


# Finds an employee by salary range.
# =============================================================================

def find_employees_by_salary_range(database: list) -> list:
    lower, upper = get_salary_range_to_search()
    search_result = []
    for employee in database:
        if lower <= float(employee["salary"]) <= upper:
            search_result.append(employee)
    if search_result == []:
        print('\nThere is no salaries within specified range.\n')
    return search_result

# Add new employee to the database.
# =============================================================================


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


# Finds an employee by his ID.
# =============================================================================
# database = read_csv('3_Homework\Homework08\DB\database.csv')


def find_employee_by_id(employees: list, id: str) -> dict:
    for employee in employees:
        if employee['id'] == id:
            return employee


# print(find_employee_by_id(database, '233'))

# Deletes an employee by his ID.
# =============================================================================
# database = read_csv('3_Homework\Homework08\DB\database.csv')


# def del_employee_by_id(database: list, id: str) -> list:
#     for employee in range(len(database)):
#         # print(database[employee])
#         for (k, v) in database[employee].items():
#             if k == 'id' and v == id:
#                 del database[employee]
#                 # print(database)


def del_employee_by_id(employees: list, employee_delete: dict) -> list:
    for employee in employees:
        if employee == employee_delete:
            # print(employee, employee_delete)
            employees.remove(employee)
            # print(employees)
            return employees
