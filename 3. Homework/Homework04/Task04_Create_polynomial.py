# Task: A natural power k is given as an input.
# Create a random list of coefficients for a polynomial, with values of
# coefficients between 0 and 100.
# Create a polynomial and write it into a file.

# ========================== OPTION 2 ==================================
# from random import randint
# import random
# k = random.randint(1, 10)

# poly = open('poly2.txt', 'a') # A file is created in the root of a project
# for i in range(k, 0, -1):
#     coef = random.randint(0, 100)
#     sign = random.choice(['+ ', '- '])
#     if coef != 0 and i != 1:
#         poly.write(f'{coef}x^{i} {sign}')
#     elif coef != 0 and i == 1:
#         poly.write(f'{coef}x {sign}')

# poly.write(f'{random.randint(0,100)} = 0\n')
# poly.close()


# ========================== OPTION 2 ==================================
from random import randint
k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
    koefs.append(randint(1, 100))

ans = list()
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
    elif k == 0:
        ans.append(f'{koefs[i]}')
    else:
        ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        ans.append('+')
    elif flag == 0:
        ans.append('-')
    k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
# Every element of ans list is written in string with '' as separator
fout.write(''.join(ans))
fout.close()
