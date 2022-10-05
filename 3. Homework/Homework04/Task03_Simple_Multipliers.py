import math
from math import sqrt
import random
input_num = 34  # random.randint(0, 10000)
print('Input number:', input_num)


# list = [1, 2, 5, 21, 22, 27, 33, 39, 29, 47, 45, 46, 48, 13, 17, 19]
# for i in list:
#     if i <= 1:
#         print('Simple or complex numbers are greater than 1.')
#     elif i == 2 or i == 5 or (i not in [21, 27, 33, 39] and i % 10 in [1, 3, 7, 9]):
#         print(i, 'simple')
#     else:
#         print(i, 'complex')

# num = 71
# for i in range(2, num+1):
#     print(num, '%', i, '=', num % i)

# exit()

# print(2, end=' ')

# 1. Create a list of simple numbers to check for input number
list = [2]
for i in range(3, input_num+1, 2):
    count = 0
    rng_stop = int(math.ceil(sqrt(i)))
    for j in range(2, rng_stop+1):
        # print(i, '%', j, '=', i % j, ', i rng_stop =', rng_stop)
        if i % j == 0:
            count += 1
            # print(count)
            break
    if count == 0:
        list.append(i)
        # print(i, end=' ')

print(list)

# 2. Create a list of simple numbers, the product of which will derive the input number
list_simple = []
for i in list:
    print(input_num, '%', i '=', input_num % i)
    # while input_num % i == 0:
    #     list_simple.append(i)
    #     input_num %= i
    #     print(i, input_num)
    # else:
    #     break

print(list_simple)
