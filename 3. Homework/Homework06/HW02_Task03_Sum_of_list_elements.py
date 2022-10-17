# Task: Create a list for N amount of numbers of the following subsequence (1 + 1/n)^n
# and output the sum of all elements of the subsequence
# Example: n = 6: [2, 2, 2, 2, 2, 3] -> 13

# ========================= ORIGINAL ==============================
# n = int(input('Enter how long the list should be: '))

# list_ = []
# sum = 0

# for i in range(n):
#     list_.append(int(round((1 + 1/(i+1)) ** (i+1), 0)))
#     sum += list_[i]

# print(f'n = {n}: {list_} -> {sum}')

# ========================= IMPROVED ==============================
n = int(input('Enter how long the list should be: '))


def f(x):
    res = int(round((1 + 1/(x+1)) ** (x+1), 0))
    return res


print(list(f(i) for i in range(n)))
