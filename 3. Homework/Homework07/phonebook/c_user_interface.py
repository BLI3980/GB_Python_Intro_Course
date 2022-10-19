# import a_data_provider as prov
from tabulate import tabulate
import b_logger as log
import a_data_read as read

# Module interacts with user:
# Asks what user wants to do, returns any output to terminal

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

def print_tables(data):
    table = 
    header1 = ['ID', 'SURNAME', 'NAME', 'PHONE', 'DESCRIPTION']
    print(tabulate(table, headers=header1,
                   tablefmt='fancy_grid', showindex='always'))

print_tables()