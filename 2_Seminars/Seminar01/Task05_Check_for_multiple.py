# Task: Create a program which take a number as an input and
# checks if the number is multiple for 5 and 10 or 15, but not 30

a = int(input('Enter a number: '))

if a == 30 or (a % 5 != 0 and a % 10 != 0 or a % 15 != 0):
    print('False')
else:
    print('True')
