# Task:
# == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# Орел и решка  
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.  
# 
# Формат входных данных На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".  
# Формат выходных данных Программа должна вывести наибольшее количество подряд выпавших Решек.  
# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3

# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7

# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == 


# ================== OPTION 1 =========================

# import random

# x = int(input('введите длину строки: '))
# O_or_P = ''
# for i in range(x):
#     gen = random.randint(0, 2)
#     if gen == 0:
#         O_or_P += 'О'
#     else:
#         O_or_P += 'Р'

# print(O_or_P)
# print(len(O_or_P))

# count = 0
# max_count = 0
# for i in range(len(O_or_P)):
#     if O_or_P[i] == 'Р':
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0

# print(max_count)

# ================== OPTION 2 =========================

# text = input("Введите произвольную последовательность букв О и Р: ")
# count = 0
# max_count = 0

# for char in text:
#     if char == "Р":
#         count += 1
#     else:
#         count = 0
#     if max_count < count:
#         max_count = count
# print(max_count)

# ================== OPTION 3 =========================

# n = input()
# total = 0
# max = 0
# for i in n:
#     if i == 'Р':
#         total += 1
#         if total > max:
#             max = total
#     else:
#         if total > max:
#             max = total

#         total = 0
# print(max)

# ================== OPTION 4 =========================

# n = input("Введите результат выпадения Орла и решки:")
# total = 0
# max = 0
# for i in n:
#     if i == 'Р':
#         total += 1
#         if total > max:
#             max = total
#     else:
#         if total > max:
#             max = total
#         total = 0
# print(max)

# ================== OPTION 5. TEACHER'S VERSION =========================

s = input()
t = 0
while "Р"*(t+1) in s:
    t += 1
if t != 0:
    print(t)
else:
    print(0)
