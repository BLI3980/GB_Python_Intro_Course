# Task: Напишите функцию triangle(a, b, c), которая принимает на вход три длины
# отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные:
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)
# Это треугольник

# ========================== OPTION 1 =======================================
# def triangle(a, b, c):
#     if a+b > c and a+c > b and b+c > a:
#         return print('This is a triangle')
#     else:
#         return print('This is NOT a triangle')


# a, b, c = int(input()), int(input()), int(input())
# triangle(a, b, c)

# ========================== OPTION 2 =======================================
def tr(a, b, c):
    return a + b > c and b + c > a and a + c > b


print(tr(1, 2, 3))
