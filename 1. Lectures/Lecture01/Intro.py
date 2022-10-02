# === VARIABLES ====================

# value = None

# a = 123
# b = 1.23

# print(a)
# print(b)

# value = 1234
# print(type(value))

# === PRINT WITH EXCLUSIONS======

# s = 'hello world'
# print(s)  # print string
# s = "hello 'world'"
# print(s)  # print string
# s = 'hell0 "world"'
# print(s)  # print string

# === PRINT FORMATS================
# a = 123
# b = 1.23
# s = "hello \"world\""
# print(s)  # print string
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# === BOOLEAN======================

# f = True
# print(f)

# list = [1, 2, 3, 'hello world', True]
# print(list)

# === INPUT OUTPUT==================

# print('Enter value a: ')
# By default all inputs are strings.
# Use 'int' to specify that you want variable 'a' as an integer.
# Same with 'float' and other types of variables
# a = int(input())
# print('Enter value b: ')
# b = int(input())

# print(a, ' + ', b, ' = ', a+b)

# === LOGICAL OPERATIONS===========
# >, >=, <, <=, ==, !=
# not, and, or - not to get confused with &, |, ^
# is, is not, in, not in

# f = [1, 2, 3, 4]
# # print(f)
# # print(not 2 in f)  # Operator 'in'

# is_odd = f[0] % 2 == 0
# print(is_odd)
# is_odd = not f[0] % 2
# print(is_odd)

# === BRANCHING IF, IF-ELSE========

# a = int(input('a = '))
# b = int(input('b = '))

# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Enter username: ')
# if username == 'Igor':
#     print('Wow, this is Igor!')
# elif username == 'Maria':
#     print('Hi, Igor')
# elif username == 'Ilnar':
#     print('Ilnar - top:)')
# else:
#     print('Hello, ', username)

# === WHILE LOOP===============
# original = 23
# inverted = 0

# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('That should be enough')

# print(inverted)

# === FOR LOOP ===============
# for i in 1, 2, 3, 4:
#     print(i ** 2)

# list = [1, 2, 3, 4]
# for i in list:
#     print(i ** 2)

# for i in range(1, 10, 2):  # 1. Start value inclusive; 2. End value, non-inclusive; 2. increment
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# === STRINGS =====================
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                  # с
# print(text[1])                  # ъ
# print(text[len(text)-1])        # Last element of the list
# print(text[-5])                 # 5th element from right - б
# print(text[:])                  # Entire text
# print(text[len(text)-2])        # 2nd element from right - о

# # From 2nd to 9th (non-inclusive) elements from left - ешь ещё (е - 2nd, ё - 8th)
# print(text[2:9])
# # From 6th from left to 18th from right - ещё этих мягких (е - 6th, -18th - space before х)
# print(text[6:-18])
# # From 0th element to end of string, every 6th element
# print(text[0:len(text)-1:6])
# # From 0th element to end of string, every 6th element
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]
# print(text)

# === LISTS =====================
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]

# ran = range(1, 6)
# print(type(ran))    # class 'range'
# numbers = list(ran)
# print(type(numbers))    # class 'list'
# print(numbers)          # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')  # 5 len
# print(numbers)          # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i)           # 20 4 6 8 10
# print(numbers)         # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']

# for i in colors:
#     print(i)  # red green blue

# for i in colors:
#     print(i*2)  # redred greengreen blueblue

# colors.append('gray')  # append gray to the end
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')    # Delete an element
# print(colors)           # ['green', 'blue', 'gray']
# del colors[2]           # Also deletes an element
# print(colors)           # ['green', 'blue']

# === FUNCTIONS =====================
def f(x):
    if x == 1:
        return 'Integer'
    elif x == 2.3:
        return 23
    else:
        return


arg = 2
print(type(arg))
print(f(arg))
print(type(f(arg)))
