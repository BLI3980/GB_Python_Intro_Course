# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример: *
# - Для N = 5: 1, -3, 9, -27, 81

# ================ OPTION 1 =======================
# n = int(input('Enter any number: '))

# element = -3
# for i in range(0, n):
#     print(element**i, end=" ")

# ================ OPTION 2 =======================
x = int(input('введите число: '))
count = 0
array = []
a = 1

while count < x:
    array.append(a)
    a = a * (-3)
    count += 1

print(f'{x} = {array}')
