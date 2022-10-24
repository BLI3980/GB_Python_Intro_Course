
# Takes formatted input and writes what is needed to output csv file.
# (Log).
# =======================================================================


def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())

# Takes formatted input and writes what is needed to output json file.
# (Log).
# =======================================================================


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')
# =======================================================================
