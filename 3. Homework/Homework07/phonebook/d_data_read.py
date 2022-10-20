
# Takes DB from csv file and changes it to a format we want for all
# future work.
# =======================================================================
def phonebook():
    phonebook = '3. Homework/Homework07/phonebook/DB_phone/phonebook.csv'
    return phonebook

def data_read(filename: str):
    data = []
    fields = ['Surname', 'Name', 'Phone', 'Comment']
    with open(filename, 'r', encoding='utf-8') as book:
        for line in book:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data
