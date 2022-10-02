# Task: Create a list of real numbers.
# Create a program which calculates the difference between
# min and max of decimal parts of numbers.
# However, min is not equal to zero.
# Example: [1.1, 1.2, 3.1, 5. 10.01] -> 0.19

import random

# Creating a list of random size between 3 and 9, filled with random integers between -10 to 10
rand_list = random.sample(range(-10, 11), random.randint(3, 10))
# Converting the list of integers into list of floats, rounded to two places
rand_float = [round(i*random.random(), 2) for i in rand_list]

print(f'\n{rand_float}\n')

min = 1
max = rand_float[0] % 1
for i in rand_float:
    dec = abs(i) % 1
    if dec > max:
        max = dec
    elif dec < min and dec != 0:
        min = dec

print(f'The difference between max decimal ({round(max,2)}) and min decimal,')
print(f'which is greater than zero ({round(min,2)}) equals to: {round(max - min, 2)}\n')
