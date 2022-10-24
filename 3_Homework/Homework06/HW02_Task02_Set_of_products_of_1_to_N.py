# Task: Create a program which takes number N as an input and
# outputs a set of products of numbers from 1 to N.
# Examples: n = 4, then [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)

# ============ OPTION 1 ======================
# Without creating a list
# n = int(input('Enter a number: '))

# product = 1

# for i in range(1, n+1):
#     product *= i
#     print(product, end=" ")

# ============ OPTION 2 ======================
# With a list
# n = int(input('Enter a number: '))

# set = []
# value = 1
# for i in range(1, n+1):
#     value = value * i
#     set.append(value)

# print(f'The resulting set of products of {5} elements is {set}')

# ============ IMPROVED ======================
n = int(input('Enter a number: '))


def f(x): return x if x == 1 else x*f(x-1)


lst = [f(i) for i in range(1, n+1)]
print(lst)
