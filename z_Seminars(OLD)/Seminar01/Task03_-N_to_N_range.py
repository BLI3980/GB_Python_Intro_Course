# Task: create a program which takes as an input number N and outputs the range from -N to N
# Example: N = 4 -> -4 -3 -2 -1 0 1 2 3 4


# ===========Option 1==================
# n = int(input('Enter a number: '))

# for i in range(-n, n+1):
#     print(i, end=" ")

# ===========Option 2==================
n = int(input('Enter a number: '))
print(list(range(-n, n+1)))

# ===========Option 3==================
# n = int(input('Enter a number: '))
# m = -n
# while (m <= n):
#     print(m, end=" ")
#     m += 1
