# Task: преобразовать список таким образом

# a = [4, 3, -10, 1, 7, 12]  ->  [4, -10, 12, 3, 1, 7]

# ================== OPTION 1 ============================
# a = [4, 3, -10, 1, 7, 12]
# b = [i for i in a if i % 2 == 0]
# c = [i for i in a if i % 2 != 0]
# print(a, '->', b+c)

# ================== OPTION 2 ============================

a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x % 2)
print(a)

# sort - method
# sorted - function

# ================== OPTION 2 ============================
# def tr(a, b, c):
#     return a + b > c and b + c > a and a + c > b
# print(tr(1, 2, 3))

# ================== OPTION 2 ============================
l = [i for i in range(10, 100)]
l1 = list(filter(lambda x: x % 9 == 0, l))
l2 = sum(list(map(lambda x: x**2, l1)))
print(l2)
