# Task: Create an algorithm of mixing elements of a list without the usage
# of the function 'shuffle' from the module 'random'
# ===================== OPTION 1 ============================
import random

myList = list(range(10))
print(myList)


for i in range(len(myList)-1):
    new_pos = random.randint(0, len(myList)-1)
    if new_pos == i:
        continue
    myList[i], myList[new_pos] = myList[new_pos], myList[i]
print(myList)

# ===================== OPTION 2 ============================
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a] = list[index_a], list[i]

# ===================== OPTION 3 ============================
y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
random.shuffle(y)
print(y)
