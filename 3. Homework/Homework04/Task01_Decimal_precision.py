# Task: A number and required precision are given as the input. 
# Calculate a number with given precision.
# Example: n = pi, d = 0.001 -> 3.141

# ============================= OPTION 1 ====================================
import random
import decimal

num = decimal.Decimal(input('Enter any decimal number: '))
precision = decimal.Decimal(input('Enter a precision, for example 0.001: '))

print(num.quantize(precision))

# ============================= OPTION 2 ====================================

# from math import pi

# d = int(input('enter precision: '))
# num = pi

# print(round(num, d))
