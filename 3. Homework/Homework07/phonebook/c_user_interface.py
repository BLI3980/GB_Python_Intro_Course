# import a_data_provider as prov
import b_logger as log
import a_data_read as read


# def temperature_view(sensor):
#     data = prov.get_temperature(sensor)
#     log.temperature_logger(data)
#     return data


# def pressure_view(sensor):
#     data = prov.get_pressure(sensor)
#     log.pressure_logger(data)
#     return data


# def wind_speed_view(sensor):
#     data = prov.get_wind_speed(sensor)
#     log.wind_speed_logger(data)
#     return data

def view(data):
    output = read.read_data(data)
    print('\nPHONEBOOK:\n')
    print(output)


# view('phonebook.csv')

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
