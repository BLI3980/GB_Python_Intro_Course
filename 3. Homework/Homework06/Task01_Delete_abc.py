# Task: Create a program which deletes from a text all words containing 'abc'


# with open('hw05_tsk01_inpt.txt', 'r') as input:
#     text = input.readline()
#     word = input.readline()
#     print(f'Input text is: {text} Word to search is: {word}')

# text = text.split()

# text = list(filter(lambda x: word not in x, text))
# print(f'Result text is: {text}')

# with open('hw05_tsk01_otpt.txt', 'w') as output:
#     for i in text:
#         output.write(i + ' ')


# ============================= IMPROVED ===============================
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# print(list(filter(lambda x: 'abc' not in x, input('input some text: ').split())))

# ============================= IMPROVED ===============================
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'


# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)


# my_text = del_some_words(my_text)
# print(my_text)
# ============================= IMPROVED ===============================
# list = "абвдлодоьбабвджлвбав"
# print(list)
# lis = list.replace("абв", "")
# print(lis)

# ============================= IMPROVED ===============================


def check_index(array, x):
    if array.index(x) % 2 != 0:
        return True
    else:
        return False


abc = list(map(int, input('input numbers list: ').split()))
