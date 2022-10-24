# Task: Create a program which takes as an input a number and
# returns the first digit of it's decimal part
# Examples: 6.78 -> 7; 5 -> 0; 0.34 -> 3

# ========== Option 1 ================
# a = float(input('Enter a number: '))

# if a < 0:
#     a = -a
# b = int(a * 10 % 10)

# print(b)

# ========== Option 2 ================
# import math
# a = float(input('Enter a number: '))

# num_result = a * 10

# if num_result % 10 == 0:
#     print('0')
# else:
#     print(math.floor(num_result) % 10)

# ========== Option 3 ================
a = float(input('Enter a number: '))

if a < 0:
    a = -a
b = int(a * 10 % 10)

# Difference between float 'a' and int 'a'. If equals zero - 'a' does not have decimal
if a - int(a) == 0:
    print("no decimal")
else:
    print(b)
