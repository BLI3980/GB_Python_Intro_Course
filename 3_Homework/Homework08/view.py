import os
from time import sleep
from turtle import pos
from tabulate import tabulate
# from inspect import CO_ASYNC_GENERATOR
from pathlib import Path
import csv

# Ask user to choose which database format he/she wants to use.
# =============================================================================


def choose_db_format():
    print('\nWhich database format you want to use?')
    select = int(input('Choose "1" for .csv or "2" for .json: '))
    return select

# print(choose_db_format())

# Show a menu to choose an action.
# =============================================================================


def show_menu() -> int:
    print("\n" + "=" * 35)
    print("Choose an action from the list below: ")
    print("1. Show the entire database")
    print("2. Find an employee")
    print("3. Show a list of employees by position")
    print("4. Show a list of employees by salary range")
    print("5. Add employee")
    print("6. Delete employee")
    print("7. Edit employee details")
    print("8. Export data into json file")
    print("9. Export data into csv file")
    print("10. End the work")
    print("=" * 35 + "\n")
    return int(input("Enter a number of corresponding action: "))

# Ask user to provide employee search last name and first name.
# =============================================================================


def get_surname_name_to_search() -> str:
    surname = input('\nEnter the surname of an employee: ')
    first_name = input('Enter the first name of an employee: ')
    return (surname, first_name)
    # return f'{last_name}, {first_name}'

# Ask user to provide position name to find a list of employees.
# =============================================================================


def get_position_to_search() -> str:
    position = input('\nEnter the name of position to search: ')
    return (position)

# Ask user to provide the range of salaries to search a list of employees.
# =============================================================================


def get_salary_range_to_search() -> str:
    lower = float(input('\nEnter the lower limit of a range to search: '))
    upper = float(input('Enter the upper limit of a range to search: '))
    return (lower, upper)


# Ask user to provide new employee details.
# =============================================================================


# def get_new_employee_details() -> str:
#     id = input('\nAssign an id to new employee: ')
#     surname = input('Enter the surname of new employee: ')
#     name = input('Enter the name of new employee: ')
#     last_name = input('Enter the last name of new employee: ')
#     position = input('Enter the position of new employee: ')
#     phone_number = input('Enter the phone number of new employee ')
#     salary = input('Enter the salary of new employee ')
#     return (id, surname, name, last_name, position, phone_number, salary)


def get_new_employee_details() -> list:
    new = {}
    new['id'] = input('\nAssign an id to new employee: ')
    new['surname'] = input('Enter the surname of new employee: ')
    new['name'] = input('Enter the name of new employee: ')
    new['last_name'] = input('Enter the last name of new employee: ')
    new['position'] = input('Enter the position of new employee: ')
    new['phone_number'] = input('Enter the phone number of new employee ')
    new['salary'] = input('Enter the salary of new employee: ')
    return (new)


# print(get_new_employee_details())


# Ask user to provide new employee details.
# =============================================================================

def get_search_id() -> str:
    return input('Enter id of employee to edit or delete: ')


# print(f'Found id: {get_search_id()}')

# Ask user to provide employee details to edit/change.
# =============================================================================
def get_change_values(employee_to_edit: dict, id: str) -> dict:
    fields = ['surname', 'first_name', 'last name',
              'position', 'phone_number', 'salary']
    old_values = employee_to_edit
    new_values = {'id': id}
    for item in fields:
        answer = input(f'Do you want to change "{item}" (Y/N)?: ')
        if answer.lower() == 'y':
            new_values[item] = input(f'Enter the new value for "{item}": ')
            # print(new_values[item])
        else:
            new_values[item] = old_values[item]
        # if answer == 1:
        #     # fields[item] == input(f'Enter the new value for "{item}":')
        #     print(fields[item])
    return new_values

# Print database in simple format.
# =============================================================================


def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)


# Print database in tabulated format.
# =============================================================================


def print_table(database: list) -> None:
    table = []
    temp = []
    for dict in database:
        for value in dict.values():
            # Get a list of values from each dictionary.
            temp.append(value)
        # Get a list of lists.
        table.append(temp)
        temp = []
    header1 = ['ID', 'SURNAME', 'NAME',
               'LAST NAME', 'POSITION', 'PHONE', 'SALARY']
    print(tabulate(table, headers=header1,
                   tablefmt='fancy_grid', showindex='false'))
    sleep(1)
