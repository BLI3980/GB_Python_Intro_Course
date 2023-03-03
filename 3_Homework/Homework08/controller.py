import os
from view import (show_menu, choose_db_format, print_table, 
                    get_new_employee_details,
                    get_search_id, get_change_values)
from model import (read_csv, read_json, write_csv, write_json,
                   find_employee_by_surname_name, find_employees_by_position,
                   find_employees_by_salary_range, find_employee_by_id,
                   del_employee_by_id, list_of_ids, export_csv, export_json)


# source_csv = '3_Homework\Homework08\DB\database.csv'
source_csv = 'C:\_GB\\3_Python\\3_Homework\Homework08\DB\database.csv'
# source_json = '3_Homework\Homework08\DB\database.json'
source_json = 'C:\_GB\\3_Python\\3_Homework\Homework08\DB\database.json'


def work_with_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    select_db = choose_db_format()
    if select_db == 1:
        source = source_csv
        database = read_csv(source)
    elif select_db == 2:
        source = source_json
        database = read_json(source)
    choice = show_menu()
    while (choice != 10):
        os.system('cls' if os.name == 'nt' else 'clear')
        # 1. All employees.
        if choice == 1:
            if select_db == 1:
                print_table(read_csv(source))
            elif select_db == 2:
                print_table(read_json(source))
        # 2. Employee(s) by surname and name.
        elif choice == 2:
            employee = find_employee_by_surname_name(database)
            print_table(employee)
        # 3. Employee(s) by position.
        elif choice == 3:
            position = find_employees_by_position(database)
            print_table(position)
        # 4. Employee(s) by salary range.
        elif choice == 4:
            salary_range = find_employees_by_salary_range(database)
            print_table(salary_range)
        # 5. Add new employee
        elif choice == 5:
            ids = list_of_ids(database)
            new = get_new_employee_details(ids)
            database.append(new)
            if select_db == 1:
                write_csv(source, database)
            elif select_db == 2:
                write_json(source, database)
            print('\nEmployee record is added. See entire table to verify that.')
        # 6. Delete employee
        elif choice == 6:
            ids = list_of_ids(database)
            id = get_search_id(ids)
            employee_to_delete = find_employee_by_id(database, id)
            deleted = del_employee_by_id(database, employee_to_delete)
            if select_db == 1:
                write_csv(source, deleted)
            elif select_db == 2:
                write_json(source, deleted)
            print('\nEmployee record is deleted. See entire table to verify that.')
        # 7. Edit employee
        elif choice == 7:
            ids = list_of_ids(database)
            id = get_search_id(ids)
            employee_to_edit = find_employee_by_id(database, id)
            updated_details = get_change_values(employee_to_edit, id)
            deleted = del_employee_by_id(database, employee_to_edit)
            database.append(updated_details)
            if select_db == 1:
                write_csv(source, database)
            elif select_db == 2:
                write_json(source, database)
            print('\nEmployee record is updated. See entire table to verify that.')
        elif choice == 8:
            export_csv(database)
        elif choice == 9:
            export_json(database)
        choice = show_menu()


