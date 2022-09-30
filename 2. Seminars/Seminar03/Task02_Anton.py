# Task:
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных В первой строке подаётся число  n – количество холодильников.
# В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры,
# в каждой строке от  5 до 100 символов.

# Формат выходных данных Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1: 6 222anton456 a1n1t1o1n1 0000a0000n00t00000o000000n gylfole richard ant0n
# Sample Output 1: 1 2 3

# Sample Input 2: 9 osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen anton aoooooooooontooooo elelelelelelelelelel ntoneeee tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2: 1 2 7 8
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==


fridges = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
           'anton',
           'aoooooooooontooooo',
           'elelelelelelelelelel',
           'ntoneeee',
           'tonee',
           '253235235a5323352n25235352t253523523235oo235523523523n',
           'antoooooooooooooooooooooooooooooooooooooooooooooooooooon',
           'unton'
           ]

# fridges = ['222anton456', 'a1n1t1o1n1',
#            '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']

virus = list(input('Enter that hacker\'s name: ').lower())

# def Search_Anton(list_to_search, name):  # Searching for Anton in fridge name
#     for i in name:
#         if i in list_to_search:
#             found = True
#             d = list_to_search.index(i)
#             del list_to_search[:d+1]
#         else:
#             found = False
#             return found
#     if found:
#         return found

# for i in range(len(fridges)):
# search_str = list(fridges[i])
# if Search_Anton(search_str, anton):
#     print(i+1, end=' ')


def Search_Virus(list_to_search, name):  # Searching for Anton in fridge name
    for i in range(len(list_to_search)):  # Going through all strings in the list of fridges
        word = list(list_to_search[i])
        for j in name:                   # Looking for each letter of the name in each string
            if j in word:
                found = True
                d = word.index(j)
                del word[:d+1]
            else:
                found = False
                break
        if found:
            print(i+1, end=' ')


Search_Virus(fridges, virus)
