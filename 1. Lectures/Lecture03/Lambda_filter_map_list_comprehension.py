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
# for i in range(1, 21):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# # same as above:
# list = [i for i in range(2, 21, 2)]
# print(list)
# # list of tules:
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

# task:
list = [1, 2, 3, 5, 16, 19, 22]
def f(i): return i**2


list_res = [(i, f(i)) for i in list if i % 2 == 0]
print(list_res)
