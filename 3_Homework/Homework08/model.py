import json
import csv
from view import (get_surname_name_to_search,
                  get_position_to_search, get_salary_range_to_search)


# Uploads DB file in csv extension and outputs it to the format we like.
# =======================================================================
def read_csv(database: str) -> list:
    employees = []
    employees1 = []
    dict1 = {}
    fields = ['id', 'surname', 'first_name', 'last_name',
              'position', 'phone_number', 'salary']
    with open(database, 'r', encoding='utf-8') as book:
        for line in book:
            record = dict(zip(fields, line.strip().split(',')))
            employees.append(record)

    for dictionary in employees:
        for (key, value) in dictionary.items():
            if value.isdigit():
                value = int(value)
                dict1[key] = value
            else:
                dict1[key] = value
        employees1.append(dict1)
        dict1 = {}
    return employees1

# Uploads DB file in json extension and outputs it to the format we like.
# =======================================================================


def read_json(database: str) -> list:
    employees = []
    with open(database, 'r', encoding='utf-8') as book:
        for line in book:
            temp = json.loads(line.strip())
            employees.append(temp)
    return employees


# Takes existing database in csv format re-writes it back to database file.
# =============================================================================


def write_csv(database: str, updates: list) -> list:
    with open(database, 'w', encoding='utf-8', newline='') as output:
        csv_writer = csv.writer(output)
        for row in updates:
            csv_writer.writerow(row.values())


# Takes existing database in json format re-writes it back to database file.
# =============================================================================


def write_json(database: str, updates: list):
    with open(database, 'w', encoding='utf-8') as output:
        for row in updates:
            output.write(json.dumps(row) + '\n')


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


# Finds an employee by his ID.
# =============================================================================


def find_employee_by_id(employees: list, id: str) -> dict:
    for employee in employees:
        if employee['id'] == id:
            return employee


# Deletes an employee by his ID.
# =============================================================================


def del_employee_by_id(employees: list, employee_delete: dict) -> list:
    for employee in employees:
        if employee == employee_delete:
            employees.remove(employee)
            return employees


# The list of ids in database.
# =============================================================================


def list_of_ids(database: list) -> list:
    ids = []
    for record in database:
        ids.append(int(record['id']))
    return ids


# Exports database into a new csv file.
# =============================================================================


def export_csv(database: list):
    name = input('Enter the name of file you want to create: ')
    file_to_save = '3_Homework\Homework08\DB\\' + name + '.csv'

    with open(file_to_save, 'w', encoding='utf-8', newline='') as output:
        csv_writer = csv.writer(output)
        for row in database:
            csv_writer.writerow(row.values())
    print(f'\nDatabase has been exported to {name}.csv file')
    print(f'Check export folder: 3_Homework\Homework08\DB\ ')


# Exports database into a new json file.
# =============================================================================


def export_json(database: list):
    name = input('Enter the name of file you want to create: ')
    file_to_save = '3_Homework\Homework08\DB\\' + name + '.json'

    with open(file_to_save, 'w', encoding='utf-8') as output:
        for row in database:
            output.write(json.dumps(row) + '\n')
    print(f'\nDatabase has been exported to {name}.json file')
    print(f'Check export folder: 3_Homework\Homework08\DB\ ')
