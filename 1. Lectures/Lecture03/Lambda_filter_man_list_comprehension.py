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

# # ========================================================
def sum(x, y):
    return x+y


def mult(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))  # Either or
    # return (op(a, b))  #Either or


calc(mult, 10, 20)  # Either or
# print(calc(sum, 10, 20))  #Either or
