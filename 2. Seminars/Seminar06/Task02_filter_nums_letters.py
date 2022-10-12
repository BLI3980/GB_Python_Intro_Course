# 2. Дан список, вывести отдельно буквы и цифры.

# ======================= OPTION 1 ====================================
# list1 = [1, 'e', 't', 's', 3, 5, 'f', 6, 'a', 9]

# nums = [i for i in list1 if type(i) == int]
# print(nums)

# letters = [i for i in list1 if type(i) != int]
# print(letters)

# ======================= OPTION 2 ====================================
a = ("a", 'b', '2', '3', 'c')
b = ('a', 'b', 'c')
c = ('1', '2', '3')


b = filter(str.isalpha, a)
c = filter(str.isdigit, a)

print(*b)
print(*c)
