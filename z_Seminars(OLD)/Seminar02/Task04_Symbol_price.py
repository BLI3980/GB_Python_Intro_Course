# Стоимость строки

# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ(в том числе пробел) стоит
# 60
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести стоимость строки.

# Тестовые данные
# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.
# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.
# ================ OPTION 1 =====================================
sum = len("Тимур - лучший математик на свете!!")*60/100
rub = int(sum)
# kop = int(round((sum - rub), 2)*100)
kop = int(sum * 100 % 100)
print(rub, "руб.", kop, "коп.")

# ================ OPTION 2 =====================================
# str = input("Введите строку: ")
# price = len(str) * 60

# print(f'Строка стоит: {price // 100} р. {price % 100} коп.')

# ================ OPTION 3 =====================================
# a = input()
# b = (len(a)*60)//100
# c = (len(a)*60)-b*100
# print(b, "р.", c, "коп.")
