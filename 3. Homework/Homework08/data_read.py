import json
import csv


def read_json() -> list:
    employee = []
    with open('database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


print(read_json())
