import os
from time import sleep
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
    print("\n" + "=" * 20)
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
    position = input('\nEnter the name of position to search: \n')
    return (position)

# Ask user to provide the range of salaries to search a list of employees.
# =============================================================================


def get_salary_range_to_search() -> str:
    lower = float(input('\nEnter the lower limit of a range to search: '))
    upper = float(input('Enter the upper limit of a range to search: '))
    return (lower, upper)

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
