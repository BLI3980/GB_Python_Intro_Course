# Task: Create a list of several numbers. Make a program calculates with sum of elements
# with odd indices:
# Example: [2, 3, 5, 9, 3] -> number on odd indices are 3 and 9 -> sum = 12.

import random
# Assigning a random size of the list between 5 and 9
list_size = random.randint(5, 10)


def Fill_List(size):  # Randomly filling the list with numbers in the range from 0 to 9
    rand_list = []
    for i in range(size):
        rand_list.append(random.randint(0, 10))
    return rand_list


def Sum_Evens(list):  # Calculating the sum of numbers with odd indices.
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


lst = Fill_List(list_size)
print(lst)
print(Sum_Evens(lst))
