# Task: Create a list for N amount of numbers of the following subsequence (1 + 1/n)^n
# and output the sum of all elements of the subsequence
# Example: n = 6: [2, 2, 2, 2, 2, 3] -> 13

# ========== OPTION 1. Dictionary ==============================
# n = int(input('Enter how long the list should be: '))

# dic = {}
# sum = 0

# for i in range(1, n + 1):
#     dic[i] = int(round((1 + 1/i) ** i, 0))
#     sum += dic[i]

# print(f'n = {n}: {dic} -> {sum}')

# ========== OPTION 2. List ==============================
n = int(input('Enter how long the list should be: '))

list_ = []
sum = 0

for i in range(n):
    list_.append(int(round((1 + 1/(i+1)) ** (i+1), 0)))
    sum += list_[i]

print(f'n = {n}: {list_} -> {sum}')
