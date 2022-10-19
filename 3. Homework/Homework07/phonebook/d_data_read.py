# from random import randint

# def get_temperature(sensor):
#     return randint(-20,0) if sensor else randint(0, 20)

# def get_pressure(sensor):
#     if sensor:
#         return randint(720, 750)
#     else:
#         return randint(750, 770)


# def get_wind_speed(sensor):
#     if sensor == 1:
#         return randint(0, 30)
#     else:
#         return randint(30, 50)

# def data_collection(sensor = 1):
#     return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))


# Takes DB from csv file and changes it to a formate we want for all
# future work
# =======================================================================
def data_read(filename: str):
    data = []
    fields = ['Surname', 'Name', 'Phone', 'Comment']
    with open(filename, 'r', encoding='utf-8') as book:
        for line in book:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


# print(read_data('phonebook.csv'))
