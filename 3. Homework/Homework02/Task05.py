# import random
# list1 = [0, 1, 1, 2, 4, 5, 6, 3, 9, 7]
# list2 = []

# random.shuffle(list1)
# print(list1)

# =======================================
# n = int(input())

# listik = [i for i in range(-n, n+1)]

# print(listik)

# =======================================
# f = open('file.txt')

with open("file") as f:
    lines = f.readlines()

print(lines)
