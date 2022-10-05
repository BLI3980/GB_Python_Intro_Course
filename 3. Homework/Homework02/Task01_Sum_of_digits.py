# Task: A real number is given as an input. Create a program which calculates
# the sum of all digits of the number.
# Examples: 6782 -> 23; 0.56 -> 11

# =============================== OPTION 1 ===============================================
# num = float(input('Enter any real number: '))

# num_int = int(str(num).replace('.', ''))
# sum = 0

# while num_int > 0:
#     cut_digit = num_int % 10
#     sum += cut_digit
#     num_int //= 10

# print(f'The sum of the digits of {num} are equal to {sum}')


# =============================== OPTION 2 ===============================================
# print(sum([int(i) for in input('Enter a number: ') if i.isdigit()]))

# =============================== OPTION 3 ===============================================

# num = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

# =============================== OPTION 4 ===============================================
n = float(input('Введите число - '))
while n % 1 > 0:
    n *= 10
summ = 0
while n > 0:
    summ += n % 10
    n //= 10
print(int(summ))
