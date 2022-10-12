# Task: Create a list of numbers. Write a program which will
# make a list with non-repeating elements only
# Example: [1, 2, 3, 3, 4, 5, 5] -> [1, 2, 4]

# ============================= INPUT ===============================
import random
# Create a list of random size between 3 and 10, filled with random
# integers between -10 and 10.
list1 = [random.randint(-10, 10) for i in range(random.randrange(3, 10))]
print(list1)
list2 = [i for i in list1 if list1.count(i) == 1]
print(list2)

# ============================= OPTION 1 ===============================
# list2 = []
# for i in list1:
#     count = 0
#     for j in list1:
#         if i == j:
#             count += 1
#     if count == 1:
#         list2.append(i)
# print(list2)

# ============================= OPTION 2 ===============================
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         del list2[list2.index(i)]
# print(list2)

# print("Honey, what's your hurry", end='?')

# ============================= OPTION 3 ? ===============================

list2 = [i for i in list1 if list1.count(i) == 1]
print(list2)

# ============================= OPTION 4 ===============================
# n = int(input("Введите число N: "))
# i = 2
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")
