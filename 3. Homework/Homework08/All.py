from pathlib import Path
import json
import csv

# Show a menu to choose an action
# =======================================================================


def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

# Uploads DB file in csv extension and outputs it to the format we like:
# =======================================================================


def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


# print(read_csv())

# Uploads DB file in json extension and outputs it to the format we like:
# =======================================================================


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

# Takes formatted input and writes what is needed to output csv file
# =======================================================================


def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())

# Takes formatted input and writes what is needed to output json file
# =======================================================================


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')

# Finds an employee by his ID
# =======================================================================


employees = read_csv()


def find_employee_by_id(employees: list) -> list:
    for employee in employees:
        if employee['id'] == 4:
            return employee


print(find_employee_by_id(employees))
# Finds an employee by salary range
# =======================================================================


# def find_employees_by_salary_range(employees: list) -> list:
#     result = []
#     lo, hi = get_salary_range()
#     for employee in employees:
#         if lo <= employee["salary"] <= hi:
#             result.append(employee)
#     return result


# Finds an employee by his last name
# =======================================================================
# for employee in employees:
#     if employee['last_name'] == last_name:
#         return employee
# employees = read_csv()
