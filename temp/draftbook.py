
# def quad_input():
#     try:
#         quadrant = int(input('Enter quadrant number: '))
#         if 1 <= quadrant <= 4:
#             return quadrant
#         else:
#             print('Incorrect entry. Please enter a number between 1 and 4, inclusive.')
#             return quad_input()
#     except (ValueError, TypeError):
#         print('Incorrect entry. Please enter a number between 1 and 4, inclusive.')
#         return quad_input()


# def coord_range(value):
#     if value <= 2:
#         if value == 1:
#             print('X > 0 and Y > 0')
#         else:
#             print('X < 0 and Y > 0')
#     else:
#         if value == 4:
#             print('X > 0 and Y < 0')
#         else:
#             print('X < 0 and Y < 0')

# =============================================================
# a = 1234
# # Entire time - time without seconds = getting seconds only
# print(a - (a // 60)*60)
# # Time without seconds - time without seconds
# print(a // 60 - (a // 60 // 60)*60)
# print(a // 60 // 60 - (a // 60 // 60 // 24)*24)
# print(a // 60 // 60 // 24 - (a // 60 // 60 // 24//365)*365)

# =============================================================
# import random
# n = int(input('Enter the size of the list: '))
# myList = []
# for i in range(n-1):
#     myList.append(random.randint(0, 10))
# print(myList)

# for i in range(0, 2, len(myList)-1):
#     sum += myList[i]
#     print(sum, myList[i])

# print(sum)
# =============================================================


# def mix(n):
#     for i in range(len(n)//2):
#         # a = n[i]
#         # print(n[-i-1])
#         # n[i] = n[-i-1]
#         # n[-i-1] = a
#         n[i], n[-i-1] = n[-i-1], n[i]


# n = [1, 2, 3, 4, 5, 6, 7]
# print(n)
# mix(n)
# print(n)

# То что в строках 4-6 написано, можно написать n[i], n[-i-1] = n[-i-1], n[i].
# Код будет работать так же.


# list1 = ['97', '+', '71', '-', '18', '-', 1, '-', '12']

# list2 = []
# # print(len(list1)-1)
# for i in range(len(list1)):
#     if i == 0:
#         list2.append(list1[i])
#     elif i % 2 != 0:
#         list2.append(list1[i]+str(list1[i+1]))
# print(list2)


# footballers_goals = {'Eusebio': 120, 'Cruyff': 104,
#                      'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(
#     footballers_goals.items(), key=lambda x: x[1], reverse=True)
# converted_dict = dict(sorted_footballers_by_goals)

# print(converted_dict)
# # Output: {'Pele': 150, 'Ronaldo': 132, 'Messi': 125, 'Eusebio': 120, 'Cruyff': 104}

# ========================================================================
# positions = {1: 'X', 2: 2, 3: 3, 4: 4, 5: 'X', 6: 6, 7: 7, 8: 8, 9: 'X'}

# check_X = [v for v in positions.keys() if positions[v] == 'X']
# print(check_X)

# win1, win2, win3, win4, win5, win6, win7, win8 = \
#     [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], \
#     [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]

# check1 = all(item in check_X for item in win1)
# check2 = all(item in check_X for item in win2)
# check3 = all(item in check_X for item in win3)
# check4 = all(item in check_X for item in win4)
# check5 = all(item in check_X for item in win5)
# check6 = all(item in check_X for item in win6)
# check7 = all(item in check_X for item in win7)
# check8 = all(item in check_X for item in win8)
# if check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8:
#     print('Player 1 has WON!!!')

# win =  \
#     [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
#      [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

# for i in win:
#     # print(i)
#     if i == check_X:
#         print('Player 1 has WON!!!')

# List1 = ['python', 'JS', 'c#', 'go', 'c', 'c++', 'Java']
# List2 = ['c#', 'Java', 'python']

# check = all(item in List1 for item in List2)

# if check:
#     print("The list1 contains all elements of the list2")
# else:
#     print("No, List1 doesn't have all elements of the List2.")
# ========================================================================
import sys
from termcolor import colored, cprint

positions = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

for i in positions.keys()
if positions[i] == 'X' or positions[i] == 'O':
    cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

print(f'-----------------------\n',
      positions.get(1), positions.get(2), positions.get(3),
      '\n-----------------------\n',
      positions.get(4), positions.get(5), positions.get(6),
      '\n-----------------------\n',
      positions.get(7), positions.get(8), positions.get(9),
      '\n-----------------------\n', sep='  |  ')
