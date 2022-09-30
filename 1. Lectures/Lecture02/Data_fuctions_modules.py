# colors = ['red', 'green', 'blue']
# data = open('C:/_GB/3_Python/1. Lectures/Lecture02/file.txt', 'a')
# data.writelines(colors)  # No separators will be written into the file
# data.close()

# ==================== PATH =======================================
# with open('C:/_GB/3_Python/1. Lectures/Lecture02/file.txt', 'w') as data:
#     data.write('\nLine 2\n')
#     data.write('Line 3')

# ===========================================================

# path = 'C:/_GB/3_Python/1. Lectures/Lecture02/file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# exit()

# ======================= EXTERNAL CALL ===========================
# import Intro
# print(Intro.f(1))

# import Intro as I
# print(I.f(1))


# ======================= FUNCTIONS ===========================

# def new_string(symbol, count):
#     return symbol * count


# print(new_string('!', 5)) # !!!!!
# # TypeError: new_string() missing 1 required positional argument
# print(new_string('!'))

# ===========================================================

# def new_string(symbol, count=3):
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12

# ===========================================================
# def concatenation(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res


# print(concatenation('a', 's', 'd', 'w'))  # asdw
# print(concatenation(1, 2, 3, 4))  # TypeError...

# ======================= RECURSION ===========================
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for i in range(1, 10):
#     list.append(fib(i))

# print(list)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]
