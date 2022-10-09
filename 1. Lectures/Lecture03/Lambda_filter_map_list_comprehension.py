# ========================= LAMBDA ===============================
# def f(x):
#     return x**2


# g = f
# print(f(2))
# print(g(2))
# ========================================================
# def calc1(x):
#     return x+10


# # print(calc1(10))


# def calc2(x):
#     return x*10

# # print(calc2(10))


# def math(op, x):
#     print(op(x))


# math(calc1, 10)
# math(calc2, 10)

# ========================================================
# def sum(x, y):
#     return x+y


# f = sum
# # f = lambda q, w: q+w


# def mult(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))  # Either or
#     # return (op(a, b))  #Either or


# calc(mult, 10, 20)  # Either or
# # print(calc(sum, 10, 20))  #Either or

# calc(f, 4, 5)
# calc(lambda q, w: q+w, 4, 5)

# ========================= LIST COMPREHENSION ===============================
# list = []
# for i in range(1, 21): # Create a list of even numbers
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# # same as above:
# list = [i for i in range(2, 21, 2)]
# print(list)
# # list of tuples:
# list = [(i, i) for i in range(2, 21, 2)]
# print(list)

# # using function as expression in comprehension:


# def f(x):
#     return x**3


# list = [f(i) for i in range(2, 21, 2)]
# print(list)
# # same as above, with tuple for better reading
# list = [(i, f(i)) for i in range(2, 21, 2)]
# print(list)


# ========================= LAMBDA, MAP, FILTER ===============================
# task:
# ========================================
# list = [1, 2, 3, 5, 16, 19, 22]


# def f(i): return i**2


# list_res = [(i, f(i)) for i in list if i % 2 == 0]
# print(list_res)
# ========================================
# data = '1 2 3 5 16 19 22 '

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]


# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# # same as above. Using functions for iteration and filtering
# ========================================

# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 16 19 22'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# same as above. Using MAP and LAMBDA.
# # ========================================
# list1 = [x for x in range(1, 20)]
# list1 = list(map(lambda x: x+10, list1))
# print(list1)

# same as above. Using MAP also.
# # ========================================
# data = list(map(int, input().split()))
# print(data)

# same as above. Using MAP again. Showing that iterators are used ones.
# ========================================
# data = map(int, '1 2 3 45'.split())  # Note the type is map (iterator)


# for e in data:
#     print(e)
# print('=========')
# for e in data:  # Cannot repeat iteration as input type is map (iterator)
#     print(e)

# Back to select, where. replacing them with MAP and FILTER.
# ========================================

# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 16 19 22'.split()
# # Select function can be replaced by map (iteration)
# res = map(int, data)
# # Where function can be replaced by filter
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# ZIP
# ========================================
# Example:
# zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't']) ->
# -> [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Note: same as map and filter, zip cannot work more than once
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids))
# print(data)
# # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# data = list(zip(users, ids, salary))
# print(data)
# # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# ENUMERATE
# ========================================
# Example:
# enumerate (['Kazan', 'London', 'Chicago', 'Amsterdam']) ->
# -> [(0, 'Kazan'), (1, 'London'), (2, 'Chicago'), (3, 'Amsterdam')]
# Note: same as previous enumerate cannot work more than once
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(enumerate(users))
print(data)


# ===================================================================
# ==SUMMARY: LIST COMPREHENSION. LAMBDA. MAP. FILTER. ZIP ==========
# ===================================================================
#   List of integers from selected range
# list = [i for i in range(2, 21, 2)]
#   List of tuples from selected range
# list = [(i, i) for i in range(2, 21, 2)]
#   List of numbers derived from a function from selected range
# list = [f(i) for i in range(2, 21, 2)]
#   List of tuples with number and derived number from selected range
# list = [(i, f(i)) for i in range(2, 21, 2)]


# print(list(map(lambda x: x*10, (x for x in range(1, 20)))))
