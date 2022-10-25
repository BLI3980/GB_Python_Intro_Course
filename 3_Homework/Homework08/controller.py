import os
from time import sleep
from view import (show_menu, choose_db_format,
                  print_result, print_table)
from model import (read_csv, read_json, write_csv, write_json,
                   find_employee_by_surname_name, find_employees_by_position, find_employees_by_salary_range)


# def controller():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     choice = show_menu()
#     ui.choices(choice)
#     if ui.if_continue() == 1:
#         sleep(1)
#         os.system('cls' if os.name == 'nt' else 'clear')
#         controller()
#     else:
#         sleep(1)
#         print('\n'+'='*15+' Have a good day! '+'='*15+'\n\n')
#         sleep(2)
#         os.system('cls' if os.name == 'nt' else 'clear')


# def transform_source(source):
#     if


def work_with_database():
    # Ask user to choose which database format to use.
    select = choose_db_format()
    if select == 1:
        source = '3_Homework\Homework08\DB\database.csv'
        # Get a list of dictionaries from csv database
        employees = read_csv(source)
    elif select == 2:
        source = '3_Homework\Homework08\DB\database02.json'
        employees = read_json(source)
    # print(employees)
    choice = show_menu()
    while (choice != 10):
        if choice == 1:
            # All employees.
            # print_result(employees)
            print_table(employees)
        elif choice == 2:
            # Employee(s) by surname and name.
            employee = find_employee_by_surname_name(employees)
            print_table(employee)
        elif choice == 3:
            # Employee(s) by position.
            position = find_employees_by_position(employees)
            print_table(position)
        elif choice == 4:
            # Employee(s) by salary range.
            salary_range = find_employees_by_salary_range(employees)
            print_table(salary_range)
        # elif choice == 4:
        #     user_data = get_new_user()
        #     add_user(phone_book, user_data)
        #     write_csv('phonebook.csv', phone_book)
        # elif choice == 5:
        #     file_name = get_file_name()
        #     write_txt(file_name, phone_book)
        choice = show_menu()


work_with_database()
