# colors = ['red', 'green', 'blue']
# data = open('C:/_GB/3_Python/1. Lectures/Lecture02/file.txt', 'a')
# data.writelines(colors)  # No separators will be written into the file
# data.close()

# colors = ['red', 'green', 'blue']
# data = open('file1.txt', 'w')
# data.write('new line\n')
# data.write('another new line')
# data.close

# ==================== PATH =======================================
# with open('C:/_GB/3_Python/1. Lectures/Lecture02/file.txt', 'w') as data:
#     data.write('\nLine 2\n')
#     data.write('Line 3')


# with open('file1.txt', 'w') as data:
#     data.write('line2\n')
#     data.write('line3\n')

# ===========================================================

# path = 'C:/_GB/3_Python/1. Lectures/Lecture02/file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line, end='')
# data.close


# ======================= EXTERNAL CALL ===========================
# import Intro
# print(Intro.f(1))

# import Intro as I
# print(I.f(1))

# import Intro
# print(Intro.f(1))

# import Intro as I
# print(I.f(2))


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


# def concatenation(*params):
#     # res: str = ''
#     # res: int = 0
#     res = 0
#     for item in params:
#         res += item
#     return res


# print(concatenation('a', 's', 'd', 'w'))
# print(concatenation(1, 2, 3, 4))

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

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))

# print(list)

# ======================= TUPLES ===========================
# a = (3, 4)
# print(a)  # (3, 4)
# print(a[0])  # 3
# print(a[-1])  # 4
# # a[0] = 12  # TypeError ...

# colors = ['red', 'green', 'blue']
# print(colors)  # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)  # ('red', 'green', 'blue')

# for e in t:
#     print(e, end=' ')  # red green blue

# red, green, blue = t
# print(red, green, blue)

# ======================= DICTIONARY ===========================
# dictionary = {}

# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }

# print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left'])  # ←

# for k in dictionary.keys():
#     print(k)  # Print all keys

# for v in dictionary.values():
#     print(v)  # Print all values

# for v in dictionary:
#     print(v)  # Print all keys

# for v in dictionary:
#     print(dictionary[v])  # Print all values

# del dictionary['left']  # Delete and element

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# for (k, v) in dictionary.items():
#     print(k, v)

# ======================= SET ===========================
# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'blue', 'green'}
# colors.add('red')
# print(colors)  # {'red', 'blue', 'green'}
# colors.add('gray')
# print(colors)   # {'red', 'green', 'gray', 'blue'}
# colors.remove('red')
# print(colors)  # {'gray', 'green', 'blue'}
# # colors.remove('red') #KeyError: 'red'
# colors.discard('red')  # Will not give and error if there is no such element
# print(colors)  # {'green', 'gray', 'blue'}
# colors.clear()  # {}
# print(colors)  # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)                # {1, 2, 3, 5, 8}
# u = a.union(b)
# # {1, 2, 3, 5, 8, 13, 21} adding to a whatever not exits in a, but exists in b
# print(u)
# i = a.intersection(b)
# print(i)                # {8, 2, 5} showing items that exit both in a and b
# dl = a.difference(b)
# print(dl)               # {1, 3} showing what exits in a that does not exist b
# dr = b.difference(a)
# # {13, 21} showing what exists in b that does not exist in a
# print(dr)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13} 1. union a and b; 2. comparing union to items that exist for in a and b
# print(q)

# s = frozenset(a)

# ======================= LIST. ADVANCED ===========================
# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e, end=' ')
# print()
# for e in list1:
#     print(e, end=' ')

# list1[0] = 123  # changing list1 changes list2 also

# print()
# for e in list1:
#     print(e, end=' ')
# print()
# for e in list1:
#     print(e, end=' ')

# list2[1] = 345  # changing list2 changes list1 also

# print()
# for e in list1:
#     print(e, end=' ')
# print()
# for e in list1:
#     print(e, end=' ')

list1 = [1, 2, 3, 4, 5]

print(list1.pop())
print(list1)
print(list1.pop(2))
print(list1)
print(list1.insert(2, 11))
print(list1)
print(list1.append(12))
print(list1)
