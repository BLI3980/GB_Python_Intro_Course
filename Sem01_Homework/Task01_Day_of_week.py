# Task: Create a program which takes as as input a number corresponding to day of week
# and checks if entered number corresponds to weekend
# Examples: 6 -> yes; 7 -> yes; 1 -> no

a = int(input('Enter a number corresponding to day of week: '))

if a < 1 or a > 7:
    print('There is no such day of week. Try again.')
elif 6 <= a <= 7:
    print('This is a weekend')
else:
    print('This is not a weekend')
