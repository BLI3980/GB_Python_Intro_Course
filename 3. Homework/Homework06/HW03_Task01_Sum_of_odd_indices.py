# Task: Create a list of several numbers. Make a program which calculates
# the sum of elements with odd indices:
# Example: [2, 3, 5, 9, 3] -> number on odd indices are 3 and 9 -> sum = 12.

# ========================= ORIGINAL ==============================
# import random
# # Assigning a random size of the list between 5 and 9
# list_size = random.randint(5, 10)


# def Fill_List(size):  # Randomly filling the list with numbers in the range from 0 to 9
#     rand_list = []
#     for i in range(size):
#         rand_list.append(random.randint(0, 10))
#     return rand_list


# def Sum_Evens(list):  # Calculating the sum of numbers with odd indices.
#     sum = 0
#     for i in range(1, len(list), 2):
#         sum += list[i]
#     return sum


# lst = Fill_List(list_size)
# print(f'Random list of several numbers:\n{lst}\n')
# print(f'The sum of elements on odd indices:\n{Sum_Evens(lst)}')

# ========================= IMPROVED ==============================

# my_list = [8, 5, 7, 3, 6]
# print(sum(my_list[i] for i in range(len(my_list)) if i % 2))

