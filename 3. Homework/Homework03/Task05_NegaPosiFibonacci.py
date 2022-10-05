# Task: A number N is entered through the console. Create a program,
# which calculates the list of Fibonacci numbers, including negative indices.
# Example: N = 8 -> [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# ========================== OPTION 1 ======================================
n = int(input('Enter the length of subsequence in both ways: '))


def Fibonacci(n):
    fib_pos = [0, 1]
    for i in range(2, n+1):
        fib_pos.append(fib_pos[-1] + fib_pos[-2])
    return fib_pos


def NegaFibonacci(n):
    fib_neg = [-1, 1]
    for i in range(2, n):
        fib_neg.insert(0, fib_neg[1] - fib_neg[0])
    return fib_neg


neg = NegaFibonacci(n)
pos = Fibonacci(n)
full = neg + pos
print(full)

# ========================== OPTION 2 ======================================
# n = int(input('Enter the length of subsequence in both ways: '))


# def Fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)


# def NegaFibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return NegaFibonacci(n-2) - NegaFibonacci(n-1)


# fib_pos = []
# fib_neg = [0]
# for j in range(1, n+1):
#     fib_pos.append(Fibonacci(j))
#     fib_neg.append(NegaFibonacci(j))


# fib_neg.reverse()
# full = fib_neg + fib_pos
# print(full)
