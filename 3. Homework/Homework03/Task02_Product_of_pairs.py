# Task: Create a program, which calculates the product of a pair of number of a list.
# The pair is the 1st element and last, the 2nd element and last but one, and so on.
# Examples:
# [2, 3, 4, 5, 6] -> [12, 15, 16]
# [2, 3, 5, 6] -> [12, 15]

import random
# Assigning a random size of the list between 5 and 9
list_size = random.randint(5, 10)
# Creating a random list of integers between 0 and 9
rand_list = random.sample(range(0, 10), list_size)

def Prod_Pairs(list):  # Creating new list with products of pairs
    res = []
    for i in range(len(list)//2):
        res.append(list[i] * list[len(list) - i - 1])
    if len(list) % 2 != 0:
        res.append(list[len(list)//2]**2)
    return res

print(f'The entry list is: {rand_list}')
res_list = Prod_Pairs(rand_list)
print(f'The list of products of pairs is: {res_list}')