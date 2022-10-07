# Task: A random natural number N is given by input. Create a program, which
# makes a list of prime multipliers of number N.
# Example: n = 3312 -> [2, 2, 2, 2, 3, 3, 23] (2*2*2*2*3*3*23 = 3312)

import math
from math import sqrt
import random
# Input is a random natural number from 0 to 10000
input_num = random.randint(0, 10000)
print('Input number:', input_num)


# 1. Create a list of prime numbers from 2 to sqrt(input number)
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

# 2. Create a list of prime numbers, the product of which will derive the input number
prime_list = []
num_cut = input_num
for i in list:
    if num_cut == 1:
        break
    while num_cut % i == 0 and num_cut > 1:
        prime_list.append(i)
        num_cut //= i
if prime_list[0] == input_num:
    print(f'{input_num} is a simple number.')
else:
    print(f'The list of simple multipliers for {input_num}: {prime_list}')
