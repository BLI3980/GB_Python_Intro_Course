from inspect import CO_ASYNC_GENERATOR
from pathlib import Path
import csv


with open(Path.cwd() / '3. Homework/Homework08/DB/database.csv', 'r', encoding='utf-8') as fin:
    csv_reader = csv.reader(fin)
    for row in csv_reader:
        print(row)

# print(csv_reader)
