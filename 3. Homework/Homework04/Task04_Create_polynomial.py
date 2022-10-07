# Task: A natural power k is given as an input.
# Create a random list of coefficients for a polynomial, with values of
# coefficients between 0 and 100.
# Create a polynomial and write it into a file.

import random
k = random.randint(1, 10)

poly = open('poly2.txt', 'a') # A file is created in the root of a project
for i in range(k, 0, -1):
    coef = random.randint(0, 100)
    sign = random.choice(['+ ', '- '])
    if coef != 0 and i != 1:
        poly.write(f'{coef}x^{i} {sign}')
    elif coef != 0 and i == 1:
        poly.write(f'{coef}x {sign}')

poly.write(f'{random.randint(0,100)} = 0\n')
poly.close()
