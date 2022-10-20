import d_data_read as read
from pathlib import Path


#  Reads csv file from DB and saves in to txt format.
# =======================================================================

def write_txt(filename: str):
    data = read.data_read(filename)
    with open(Path.cwd() / '3. Homework/Homework07/'
              'phonebook/DB_phone/phonebook.txt', 'w', encoding='utf-8') as txt:
        for line in data:
            for value in line.values():
                txt.writelines(value+';')
            txt.writelines('\n')


write_txt(read.phonebook())
