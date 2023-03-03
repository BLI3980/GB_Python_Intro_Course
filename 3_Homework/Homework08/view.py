from time import sleep
from tabulate import tabulate
import emoji

# Ask user to choose which database format he/she wants to use.
# =============================================================================


def choose_db_format():
    print('\nWhich database format you want to use?')
    is_OK = False
    while not is_OK:
        try:
            select = int(input('Choose "1" for .csv or "2" for .json: '))
            is_OK = True
            if select not in [1, 2]:
                is_OK = False
                print('Incorrect number. Try again.')
        except ValueError:
            print('This is not a number. Try again.')
    return select


# Show a menu to choose an action.
# =============================================================================


def show_menu() -> int:
    print("\n" + "=" * 35)
    print(emoji.emojize(":play_button:  Choose an action from the list below: "))
    print(emoji.emojize("1. :department_store: Show the entire database"))
    print(emoji.emojize("2. :magnifying_glass_tilted_left: Find an employee"))
    print(emoji.emojize(
        "3. :man_office_worker: Show a list of employees by position"))
    print(emoji.emojize(
        "4. :money_bag: Show a list of employees by salary range"))
    print(emoji.emojize("5. :NEW_button: Add employee"))
    print(emoji.emojize("6. :cross_mark: Delete employee"))
    print(emoji.emojize("7. :hammer_and_wrench:  Edit employee details"))
    print(emoji.emojize("8. :floppy_disk: Export data into csv file"))
    print(emoji.emojize("9. :dvd: Export data into json file"))
    print(emoji.emojize("10. :stop_button:  End the work"))
    print("=" * 35 + "\n")
    is_OK = False
    while not is_OK:
        try:
            select = int(input("Enter a number of corresponding action: "))
            is_OK = True
            if select not in range(1, 11):
                is_OK = False
                print('Incorrect number. Try again.')
        except ValueError:
            print('This is not a number. Try again.')
    return select


# Ask user to provide employee search last name and first name.
# =============================================================================


def get_surname_name_to_search():
    surname = input('\nEnter the surname of an employee: ')
    first_name = input('Enter the first name of an employee: ')
    return surname, first_name


# Ask user to provide position name to find a list of employees.
# =============================================================================


def get_position_to_search() -> str:
    position = input('\nEnter the name of position to search: ')
    return (position)


# Ask user to provide the range of salaries to search a list of employees.
# =============================================================================


def get_salary_range_to_search() -> float:
    is_OK = False
    while not is_OK:
        try:
            lower = float(
                input('\nEnter the lower limit of a range to search: '))
            upper = float(
                input('Enter the upper limit of a range to search: '))
            is_OK = True
        except ValueError:
            print('This is not a number. Try again.')
    return (lower, upper)


# Ask user to provide new employee details.
# =============================================================================


def get_new_employee_details(ids: list) -> list:
    new = {}
    new['id'] = if_id_exist(ids)
    new['surname'] = input('Enter the surname of new employee: ')
    new['first_name'] = input('Enter the name of new employee: ')
    new['last_name'] = input('Enter the last name of new employee: ')
    new['position'] = input('Enter the position of new employee: ')
    new['phone_number'] = input('Enter the phone number of new employee ')
    new['salary'] = input('Enter the salary of new employee: ')
    return (new)


# Ask user to provide id of employee to search.
# =============================================================================


def get_search_id(list_of_ids: list) -> int:
    is_OK = False
    ids = list_of_ids
    while not is_OK:
        try:
            number = int(input('Enter id of employee to edit or delete: '))
            is_OK = True
            if number not in ids:
                is_OK = False
                print('No employee with such id. Try again.')
        except ValueError:
            print('This is not a number. Try again.')
    return number


# Ask user to provide employee details to edit/change.
# =============================================================================


def get_change_values(employee_to_edit: dict, id: str) -> dict:
    fields = ['surname', 'first_name', 'last_name',
              'position', 'phone_number', 'salary']
    old_values = employee_to_edit
    new_values = {'id': id}
    for item in fields:
        answer = input(f'Do you want to change "{item}" (Y/N)?: ')
        if answer.lower() == 'y':
            new_values[item] = input(f'Enter the new value for "{item}": ')
        else:
            new_values[item] = old_values[item]
    return new_values


# Checks if id already exists and if not number is provided
# =============================================================================

def if_id_exist(list_of_ids: list) -> int:
    is_OK = False
    ids = list_of_ids
    while not is_OK:
        try:
            number = int(input('\nAssign an id to new employee: '))
            is_OK = True
            if number in ids:
                is_OK = False
                print('Such id already exists in database. Try again.')
        except ValueError:
            print('This is not a number. Try again.')
    print('Good choice.')
    return number


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
