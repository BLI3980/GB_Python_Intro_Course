# Two position numbers are contained in a file.txt. Number N is entered by user from console.
# Create a list of elements from -N to N. Calculate a product of elements of the list under
# positions (not indices) specified in file.txt
# Example: positions 1 and 3, n = 5: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] -> 15

# ================================= OPTION 1 ================================================
import random
n = int(input('Enter the size of the list: '))
n_list = []
for i in range(-n, n+1):  # Create a list of elements from -N to N
    n_list.append(i)

with open(r'C:/_GB/3_Python/3. Homework/Homework02/file.txt') as f:
    list_str = list(f.read().split())  # Read file as list of strings
list_pos = [int(i) for i in list_str]  # Convert list into list of integers

# Find a product of elements under position numbers from the file
product = 1
for i in list_pos:
    product *= n_list[i - 1]

print(f'The list of elements: {n_list}')
print(
    f'The product of elements under position numbers, specified in file is: {product}\n')

# ================================= OPTION 2 ================================================
n = int(input('input number '))
list = []
for i in range(n):                      # генератор случайных чисел
    a = random.randint(-n, n)
    list.append(a)
print(list)
index_list = input(
    f'введите позиции элементов от 1 до {n} через пробел').split()
result = 1
for j in range(len(index_list)):        # перебор элементов с номерами позиций
    a = int(index_list[j])-1
    print(f'{result}*{int(list[a])}', end=' ')
    result *= int(list[a])
print(f'= {result}')
