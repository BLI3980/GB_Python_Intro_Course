import json
import csv


# Uploads DB file in csv extension and outputs it to the format we like.
# (Model).
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

# Uploads DB file in json extension and outputs it to the format we like.
# (Model)
# =======================================================================


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

# Finds an employee by his ID (Model)
# =======================================================================


# employees = read_csv()


def find_employee_by_id(employees: list) -> list:
    for employee in employees:
        if employee['id'] == 4:
            return employee


# print(find_employee_by_id(employees))


# Finds an employee by salary range (Model)
# =======================================================================


# def find_employees_by_salary_range(employees: list) -> list:
#     result = []
#     lo, hi = get_salary_range()
#     for employee in employees:
#         if lo <= employee["salary"] <= hi:
#             result.append(employee)
#     return result


# Finds an employee by his last name (Model)
# =======================================================================
# for employee in employees:
#     if employee['last_name'] == last_name:
#         return employee
# employees = read_csv()
