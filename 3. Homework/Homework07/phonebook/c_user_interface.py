from tabulate import tabulate
from time import sleep
import d_data_read as book
import e_module_all_contents as all
import f_module_find_by_sn as surname
import g_module_find_by_sn_nm as name

# Module interacts with user


# Asks what user wants to dd in order to return any output to terminal
# =======================================================================
def show_menu() -> int:
    print("\nChoose the action you want to do:\n"
          "1. Show the entire phonebook\n"
          "2. Find people by surname\n"
          "3. Find a person by surname and name\n"
          "4. Find a person by phone number\n"
          "5. Add new person to the phonebook\n"
          "6. Save the phonebook in text format\n"
          "7. End the work")
    choice = int(input('Choose the corresponding number of action: '))
    return choice


# Asks if user wants to continue in order to make further action
# =======================================================================

def if_continue() -> int:
    print('\nDo you want to continue with another action (1: Yes, 2: No)?: ')
    select = int(input())
    return select


# # Choices
# # =======================================================================
# def choices(select):
#     if select == 1:
#         print_tables()
#     # if select == 2:
#     #     action2 = 2
#     # if select == 3:
#     #     action3 = 3
#     # if select == 4:
#     #     action4 = 4
#     # if select == 5:
#     #     action5 = 6

# Takes a table based on user choice and outputs it to terminal
# =======================================================================


def print_tables(choice: int) -> None:
    data = 'phonebook.csv'
    sleep(1)
    if choice == 1:
        table = all.show_all(data)
        print('\nThe entire phonebook:\n')
    elif choice == 2:
        table = surname.find_by_surname(data)
        print('\nThe Search by surname:\n')
    elif choice == 3:
        table = name.find_by_surname_name(data)
        print('\nThe Search by surname and name:\n')
    else:
        print('The rest of the work in not done yet.....')

    header1 = ['ID', 'SURNAME', 'NAME', 'PHONE', 'DESCRIPTION']
    print(tabulate(table, headers=header1,
                   tablefmt='fancy_grid', showindex='always'))
    sleep(1)


# print_tables(show_menu())
# if_continue()
