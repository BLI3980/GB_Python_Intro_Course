import os
from time import sleep
from view import (show_menu, choose_db_format,
                  print_result, print_table, get_new_employee_details,
                  get_search_id, get_change_values)
from model import (read_csv, read_json, write_csv, write_json,
                   find_employee_by_surname_name, find_employees_by_position,
                   find_employees_by_salary_range, find_employee_by_id,
                   del_employee_by_id)


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

source_csv = '3_Homework\Homework08\DB\database.csv'
source_json = '3_Homework\Homework08\DB\database02.json'


def work_with_database():
    # Ask user to choose which database format to use.
    select = choose_db_format()
    if select == 1:
        # source = '3_Homework\Homework08\DB\database.csv'
        source = source_csv
        # Get a list of dictionaries from csv database
        employees = read_csv(source)
    elif select == 2:
        # source = '3_Homework\Homework08\DB\database02.json'
        source = source_json
        employees = read_json(source)
    # print(employees)
    choice = show_menu()
    while (choice != 10):
        # 1. All employees.
        if choice == 1:
            # print_result(employees)
            print_table(read_csv(source))
        # 2. Employee(s) by surname and name.
        elif choice == 2:
            employee = find_employee_by_surname_name(employees)
            print_table(employee)
        # 3. Employee(s) by position.
        elif choice == 3:
            position = find_employees_by_position(employees)
            print_table(position)
        # 4. Employee(s) by salary range.
        elif choice == 4:
            salary_range = find_employees_by_salary_range(employees)
            print_table(salary_range)
        # 5. Add new employee
        elif choice == 5:
            new = get_new_employee_details()
            # print(type(new))
            # add_new = add_employee(new)
            # print(add_new)
            if select == 1:
                database = read_csv(source)
                database.append(new)
                print(database)
                write_csv(source, database)
            else:
                write_json(source, database)
        # 6. Delete employee
        elif choice == 6:
            id = get_search_id()
            if select == 1:
                database = read_csv(source)
                employee_to_delete = find_employee_by_id(database, id)
                deleted = del_employee_by_id(database, employee_to_delete)
                # del_employee_by_id(database, id)
                write_csv(source, deleted)
            else:
                write_json(source, database)
        # 7. Edit employee
        elif choice == 7:
            id = get_search_id()
            if select == 1:
                database = read_csv(source)
                employee_to_edit = find_employee_by_id(database, id)
                updated_details = get_change_values(employee_to_edit, id)
                deleted = del_employee_by_id(database, employee_to_edit)
                database.append(updated_details)
                write_csv(source, database)
            else:
                write_json(source, database)

        # elif choice == 5:
        #     file_name = get_file_name()
        #     write_txt(file_name, phone_book)
        choice = show_menu()
