from tabulate import tabulate
from time import sleep
import d_data_read as read
import e_module_all_contents as all
import f_module_find_by_sn as surname
import g_module_find_by_sn_nm as name
import h_module_find_by_phone as phone
import i_module_add_new as add
import j_module_output as text

# Module interacts with user.


# Asks what user wants to do with phone book.
# =======================================================================
def show_menu() -> int:
    print("\nChoose the action you want to do:\n"
          "1. Show the entire phonebook\n"
          "2. Find people by surname\n"
          "3. Find a person by surname and name\n"
          "4. Find a person by phone number\n"
          "5. Add new person to the phonebook\n"
          "6. Save the phonebook in text format")
    choice = int(input('Choose the corresponding number of action: '))
    return choice


# Asks if user wants to continue in order to make further action.
# =======================================================================

def if_continue() -> int:
    print('\nDo you want to continue with another action (1: Yes, 2: No)?: ')
    select = int(input())
    return select


# # User choices.
# # =======================================================================

def choices(choice: int) -> None:
    data = read.phonebook()
    sleep(1)
    if choice == 1:
        table = all.show_all(data)
        print('\nThe entire phonebook:\n')
        print_table(table)
    elif choice == 2:
        table = surname.find_by_surname(data)
        print('\nThe search by surname:\n')
        print_table(table)
    elif choice == 3:
        table = name.find_by_surname_name(data)
        print('\nThe search by surname and name:\n')
        print_table(table)
    elif choice == 4:
        table = phone.find_by_phone(data)
        print('\nThe search by phone number:\n')
        print_table(table)
    elif choice == 5:
        table = add.add_person()
        print('\nThese details have been added to the phonebook:\n')
        print_table(table)
    elif choice == 6:
        text.write_txt(data)
        print('\nThe output text file has been created in DB folder.\n')
    else:
        print('The other options are yet to be developed....')
    sleep(1)


# Table format for terminal.
# =======================================================================

def print_table(table: list) -> None:
    header1 = ['SURNAME', 'NAME', 'PHONE', 'DESCRIPTION']
    print(tabulate(table, headers=header1,
                   tablefmt='fancy_grid', showindex='false'))
    sleep(1)
