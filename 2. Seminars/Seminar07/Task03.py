# Task: преобразовать список таким образом:
# a = [4, 3, -10, 1, 7, 12]
# result = [4, -10, 12, 3, 1, 7]:


# ========================== OPTION 1 =======================================
# a = [4, 3, -10, 1, 7, 12]
# even = [i for i in a if i % 2 == 0]
# odd = [i for i in a if i % 2 != 0]
# result = even + odd
# print(result)

# ========================== OPTION 2 =======================================

a = [4, 3, -10, 1, 7, 12]
# sorts first by the key, then in ascending order (default sort)
a.sort(key=lambda x: x % 2)
print(a)

# Note:
# a.sort() - method
# sorted - function. original list is not changed

