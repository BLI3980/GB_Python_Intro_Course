# Task: Two polynomials are written into two files. Create a program, which
# calls for these two polynomials from the files, and outputs
# the summation of two polynomials into a new file.

import math
# ========================== OPTION 1 =========================================
# Input strings from external files:
# =======================
print('======================')
with open('poly1.txt', 'r') as poly1:
    poly1 = poly1.readline()
    # 9x^9 - 64x^8 - 72x^7 + 2x^6 - 40x^5 + 2x^4 - 1x^3 + 35x + 82 = 0
    print('Input polynomial 1:', poly1)
with open('poly2.txt', 'r') as poly2:
    poly2 = poly2.readline()
    # 78x^7 + 18x^6 - 2x^5 - 82x^3 + 45x^2 - 23x + 4 = 0
    print('Input polynomial 2:', poly2)
print('======================')

# 1. Create a list of monomials:
# =======================


def Monomials(string):
    string = string.replace(' - ', ' -')
    string = string.replace(' + ', ' +')
    string = string.replace(' = 0', '')
    string = string.split()
    return string


# # 2. Create a dictionary, where key is power, value is coefficient of
# # of the polynomial
# # =======================


def Dict(monomial):
    dict = {}
    for item in monomial:
        if item.find('x') > 1 and item.find('^') > -1:
            coef = int(item[:item.find('x')])
            power = int(item[item.find('x')+2:])
            dict[power] = coef
        elif item.find('x') > 1 and item.find('^') == -1:
            coef = int(item[:item.find('x')])
            power = 1
            dict[power] = coef
        elif item.find('x') == 0:
            coef = 1
            power = int(item[item.find('x')+2:])
            dict[power] = coef
        elif item.find('x') == 1 and item[item.find('x')-1] != '-':
            coef = int(item[:item.find('x')])
            power = int(item[item.find('x')+2:])
            dict[power] = coef
        elif item.find('x') == 1 and item[item.find('x')-1] == '-':
            coef = -1
            power = 1
            dict[power] = coef
        else:
            dict[0] = int(item)
    return dict


# 3. Create a dictionary of summations of two polynomials
# =======================


def Dict_Sum(dict1, dict2):
    result_dict = {}
    if len(dict1) < len(dict2):
        dict1, dict2 = dict2, dict1
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            # print(key1, key2)
            if key1 == key2:
                result_dict[key1] = dict1[key1] + dict2[key2]
                break
            elif key2 not in dict1.keys():
                result_dict[key2] = dict2[key2]
            else:
                result_dict[key1] = dict1[key1]
    reversed_sorted = dict(reversed(sorted(result_dict.items())))
    return reversed_sorted


# 4. Finally. printout the sum of polynomials
# =======================


def Print_Summ(dict):
    for (k, v) in dict.items():
        if k == max(dict.keys()):
            print(f'{v}x^{k}', end='')
        elif v < 0 and k > 1:
            print(f' - {int(math.fabs(v))}x^{k}', end='')
        elif v > 0 and k > 1:
            print(f' + {v}x^{k}', end='')
        elif v > 0 and k == 1:
            print(f' + {v}x', end='')
        elif v < 0 and k == 1:
            print(f' - {int(math.fabs(v))}x', end='')
        elif v > 0 and k == 0:
            print(f' + {v}', end='')
        elif v < 0 and k == 0:
            print(f' - {int(math.fabs(v))}', end='')
    print(' = 0')


# 5. Output calls:
# =======================
monom_list1 = Monomials(poly1)
dictionary1 = Dict(monom_list1)
monom_list2 = Monomials(poly2)
dictionary2 = Dict(monom_list2)
polynomials_sum = Dict_Sum(dictionary1, dictionary2)

print('The sum of polynomials: ', end='')
Print_Summ(polynomials_sum)
print('======================')

# 6. Write to external file:
# =======================
with open('poly_sum.txt', 'w') as result:
    for (k, v) in polynomials_sum.items():
        if k == max(polynomials_sum.keys()):
            result.write(f'{v}x^{k}')
        elif v < 0 and k > 1:
            result.write(f' - {int(math.fabs(v))}x^{k}')
        elif v > 0 and k > 1:
            result.write(f' + {v}x^{k}')
        elif v > 0 and k == 1:
            result.write(f' + {v}x')
        elif v < 0 and k == 1:
            result.write(f' - {int(math.fabs(v))}x')
        elif v > 0 and k == 0:
            result.write(f' + {v}')
        elif v < 0 and k == 0:
            result.write(f' - {int(math.fabs(v))}')
    result.write(' = 0')

# ========================== OPTION 2 =========================================
# From the lecturer:
# Option only works if size and powers are the same in both polynomials

# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close
