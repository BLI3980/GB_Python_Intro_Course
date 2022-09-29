# Task: Create an algorithm of mixing elements of a list without the usage
# of the function 'shuffle' from the module 'random'

import random

myList = list(range(10))
print(myList)


for i in range(len(myList)-1):
    new_pos = random.randint(0, len(myList)-1)
    if new_pos == i:
        continue
    myList[i], myList[new_pos] = myList[new_pos], myList[i]
print(myList)
