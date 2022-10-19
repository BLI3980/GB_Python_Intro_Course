# Task: Create a list of numbers. Write a program which will
# make a list with non-repeating elements only
# Example: [1, 2, 3, 3, 4, 5, 5] -> [1, 2, 4]

# ============================= INPUT ===============================
# list1 = [1, 2, 3, 3, 4, 5, 5]

# print(list1)
# ============================= ORIGINAL 1 ===============================
# list2 = []
# for i in list1:
#     count = 0
#     for j in list1:
#         if i == j:
#             count += 1
#     if count == 1:
#         list2.append(i)
# print(list2)

# ============================= ORIGINAL 2 ===============================
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         del list2[list2.index(i)]
# print(list2)

# ============================= IMPROVED ===============================

# list2 = [i for i in list1 if list1.count(i) == 1]
# print(list2)

# ============================= IMPROVED ===============================
# result_list = list(filter(lambda a: list1.count(a) == 1, list1))
# print(list2)

# ============================= IMPROVED ===============================
# numbers = [2, 3, 4, 5, 6, 7, 5]
# # a = len(numbers)
# # b = len(numbers)//2
# # c = len(numbers)//2-1
# # print(a, b, c)
# numbers1 = numbers[:(len(numbers)//2)-1:-1]
# print(numbers1)
# diff = list([a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])])
# print(diff)
