import random
list1 = [random.randint(-10, 10) for i in range(random.randrange(3, 10))]
print(list1)

# list2 = set(list1)
# print(list2)

list2 = set()
for i in list1:
    if i is not list2:
        list2.add(i)
    else:
        list2.remove(i)
print(list2)

list3 = {}
for i in range(len(list1)):
    if list[i] is not list3:
        list3[list1[i]] = list1[i]
    else:
        list3.remove(list1[i])
print(list3)
