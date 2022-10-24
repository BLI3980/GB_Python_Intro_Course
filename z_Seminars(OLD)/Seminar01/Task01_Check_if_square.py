# Task: Create a program which take two numbers from user input and checks if one of them is Power of the other
# Examples: 5, 25 -> yes; 4, 16 -> yes; 25, 5 -> yes; 8, 9 -> no

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

if a == b**2 or b == a**2:
    print('One number is square of the other.')
else:
    print('None of these two numbers is square of the other.')
