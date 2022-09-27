# Task: Create a program which takes a user input of five numbers and find which one of them is the largest
# Example:
# 1, 4, 8, 7, 5 -> 8

print('Enter any five numbers: ')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a, b, c, d, e]
# list = list(map(int, input('enter five number separated by space: ').split())) # Alternative way of declaring a list
# largest = list[0]

for i in range(1, len(list)):
    if list[i] > largest:
        largest = list[i]

print(largest)

# print(max(a, b, c, d, e)) # Another alternative solution
