# Task: Задайте список. Напишите программу, которая определит, присутствует 
# ли в заданном списке строк некое число.

list1 = ["1", "another string", "string 3", "hello world", "123"]
print(list1)

num_to_find = int(input('Enter the number to search: '))
found = False
for word in list1:
    if str(num_to_find) in word:
        found = True
        break
if found:
    print('Yes, this number is present in the list.')
else:
    print('No, this number is not in the list.')


