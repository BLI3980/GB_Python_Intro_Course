
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


