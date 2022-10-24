# Task: Create a program for checking if the following statement is true for all
# values of predicates:
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
a = not (x or y or z) == (not x and not y and not z)

print(a)
