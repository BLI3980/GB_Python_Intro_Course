# Task: Напишите программу, которая подсчитывает сумму квадратов всех
# двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum
# Обратите внимание: на 9 должно делиться исходное двузначное число,
# а не его квадрат


# ========================== OPTION 1a =======================================
# input = [23, 63, 2, 81, 34, 234]
# two_digit_9 = list(filter(lambda x:  9 < x < 100 and not x % 9, input))
# power2 = list(map(lambda x: x**2, two_digit_9))
# summ = sum(power2)
# print(two_digit_9)
# print(power2)
# print(summ)

# ========================== OPTION 1b =======================================
# l_value = [23, 63, 2, 81 ,34, 234]
# l_value = filter(lambda x: (9 < x < 100) and (x % 9 == 0),  l_value)
# l_value = map(lambda x: x**2, l_value)
# print(sum(l_value))

# ========================== OPTION 2 =======================================
# For ALL two-digit numbers:
# input = list(filter(lambda x: x % 9 == 0, list(range(10, 100))))
# input = list(map(lambda x: x**2, input))
# input_sum = sum(input)

# ========================== OPTION 3 =======================================
# l = [i for i in range(10, 100)]
# l1 = list(filter(lambda x: x % 9 == 0, l))
# l2 = sum(list(map(lambda x: x**2, l1)))
# print(l2)
