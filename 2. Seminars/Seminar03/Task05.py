# Task:

import random
n = int(input('Enter the a number: '))
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

myList = []
for i in range(n):  # Create randomly filled list of N elements.
    myList.append(random.randint(0, 10))

# Create randomly filled list of N elements.
mylist1 = [random.randint(0, 10) for i in range(n)]
