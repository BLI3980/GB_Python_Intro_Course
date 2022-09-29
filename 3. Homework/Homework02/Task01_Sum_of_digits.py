# Task: A real number is given as an input. Create a program which calculates
# the sum of all digits of the number.
# Examples: 6782 -> 23; 0.56 -> 11

num = float(input('Enter any real number: '))

num_int = int(str(num).replace('.', ''))
sum = 0

while num_int > 0:
    cut_digit = num_int % 10
    sum += cut_digit
    num_int //= 10

print(f'The sum of the digits of {num} are equal to {sum}')
