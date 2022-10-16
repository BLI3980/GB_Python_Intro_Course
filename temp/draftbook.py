# ====================== Colors ==============================
# print("\033[31mThis is red font.\033[0m")
# print("\033[32mThis is green font.\033[0m")
# print("\033[33mThis is yellow font.\033[0m")
# print("\033[34mThis is blue font.\033[0m")
# ====================== Rules ==============================
# ===========================================================

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
# import sys
# from termcolor import colored, cprint

# positions = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

# for i in positions.keys()
# if positions[i] == 'X' or positions[i] == 'O':
#     cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

# print(f'-----------------------\n',
#       positions.get(1), positions.get(2), positions.get(3),
#       '\n-----------------------\n',
#       positions.get(4), positions.get(5), positions.get(6),
#       '\n-----------------------\n',
#       positions.get(7), positions.get(8), positions.get(9),
#       '\n-----------------------\n', sep='  |  ')
# ========================================================================

# def Exceptions(num, candies):
#     while True
#     try:
#         int(num)
#         print(num)
#         try:
#             # 1 < int(num) < min(candies, 28)
#             int(num) == 8
#             # print(type(int(num)), num, min(candies, 28))
#             # return int(num)
#         except:
#             print(num)
#             print('You cannot take this amount of candies.')
#             print(
#                 f'Please take [\033[31m1 .. {min(candies, 28)}\033[0m] candies: ', end='')
#             num = input()
#             Exceptions(num, candies)
#         else:
#             return int(num)
#     except ValueError:
#         print(
#             f'Please enter and integer number [1 .. {min(candies, 28)}]: ', end='')
#         num = input()
#         Exceptions(num, candies)
#     else:
#         return int(num)


# def IsNum(type: str, num: str):
#     try:
#         type(num)
#         return True
#     except:
#         return False


# def EntryCheck(type=int):
#     num = input('Enter a number: ')
#     while not IsNum(type, num):
#         num = input('This is not a number. Please enter an integer number: ')
#     return int(num) * 2


# print(EntryCheck())


# def IsNum(type: str, num: str):
#     try:
#         type(num)
#         return True
#     except:
#         return False


# def EntryCheck(type=int):
#     num = input('Enter a number: ')
#     while not IsNum(type, num):
#         num = input('This is not a number. Please enter an integer number: ')
#     return int(num) * 2


# def InRange(num, amount):
#     while not 1 < num < min(amount, 28):
#         print('num = ', num, 'amount = ', amount)
#         print('Number is out of allowed range. Please try again. ')
#         InRange(EntryCheck(), 250)
#     else:
#         return num


# # print(IsNum())
# # print(EntryCheck())
# print(InRange(EntryCheck(), 250))


# def EntryCheck(num: str, amount, type=int):
#     try:
#         1 < type(num) < min(amount, 28)
#         return True
#     except ValueError:
#         print('This is not a number.')
#         return False
#     except:
#         print('Number is outside allowed range.')
#         return False


# def EntryOk():
#     num = ('Enter a number: ')
#     while not EntryCheck(num, 250):
#         print('Wrong entry. Please try again.')
#     else:
#         print(type(num), num)
#         return num


# print(EntryOk())


# def getNumber01():  # Первый вариант
#     while type:
#         getNumber = input('Введите число: ')   # Ввод числа
#         try:                                   # Проверка что getTempNumber преобразуется в число без ошибки
#             int(getNumber)

#         # Проверка на ошибку неверного формата (введены буквы)
#         except ValueError:
#             print('"' + getNumber + '"' + ' - не является числом')
#         else:                                  # Если getTempNumber преобразован в число без ошибки, выход из цикла while
#             break
#     # возвращает модуль getTempNumber (для искл. отрицат. чисел)
#     return getNumber


# # print(getNumber01())


# def InRange():
#     temp = getNumber01
#     # temp = int(input('Enter the number: '))
#     print(type(temp), temp)
#     while not 1 < temp < 28:
#         print('Number is outside the range.')
#         temp = getNumber01
#         # temp = int(input('Enter the number: '))
#     else:
#         return temp


# print(InRange())

# ============ Exceptions for Candy game ================================


# def protectinput(maxcand=28):
#     num = input(f'Введите число конфет: ')
#     while not num.isdigit():
#         print('This is not a number.')
#         num = input(f'Введите число конфет: ')
#     if 0 < int(num) < maxcand + 1:
#         return num
#     else:
#         return protectinput()


# print(protectinput())


# def CheckInput():
#     input_num = input('Enter a number: ')
#     while not input_num.isdigit():
#         # print('This is not a number. Please try again.', end='')
#         input_num = input('Wrong entry. Please try again: ')
#     max_take = min(100, 28)
#     if 0 < int(input_num) < max_take:
#         return int(input_num)
#     else:
#         return CheckInput()


# print(CheckInput())

# ============ Exceptions for XO game ================================


# def take_input(player_token, board):
#     valid = False
#     while not valid:
#         player_answer = input(
#             f'Куда поставим {player_token}? Введите число 1 - 9: ')
#         try:
#             player_answer = int(player_answer)
#         except:
#             print('Некорректный ввод. Вы уверены, что ввели число?')
#             continue
#         if 1 <= player_answer <= 9:
#             if (str(board[player_answer - 1]) not in 'XO'):
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print('Эта клетка уже занята!')
#         else:
#             print('Некорректный ввод. Введите число от 1 до 9')
# ===================================================================
