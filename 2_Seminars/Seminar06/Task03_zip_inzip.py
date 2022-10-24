# 3. Преобразовать набора списков
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# в другой набор['user1', 4, 111]['user2', 5, 222]['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# ======================= OPTION 1 ====================================
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

# users1 = [i[0] for i in data]
# ids1 = [i[1] for i in data]
# salary1 = [i[2] for i in data]
# print(users1, ids1, salary1, sep='\n')

# ======================= OPTION 2 ====================================
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

a, b, c = map(list, zip(users, ids, salary))
print(a, b, c, sep="\n")
a, b, c = map(list, zip(a, b, c))

print(a, b, c, sep="\n")

# ======================= OPTION 3 ====================================
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# for i in zip(users, ids, salary):
#     print(i)

# users_1, ids_1, salary_1 = map(list, zip(*zip(users, ids, salary)))

# print(users_1, ids_1, salary_1 + '\n')
