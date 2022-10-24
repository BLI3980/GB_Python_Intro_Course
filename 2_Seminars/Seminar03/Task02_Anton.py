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

# ==================== INPUTS ===========================================
# Sample input 1:
fridges = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
           'anton',
           'aoooooooooontooooo',
           'elelelelelelelelelel',
           'natonneeee',
           'tonee',
           '253235235a5323352n25235352t253523523235oo235523523523n',
           'antoooooooooooooooooooooooooooooooooooooooooooooooooooon',
           'unton'
           ]

# Sample input 2:
# fridges = ['222anton456', 'a1n1t1o1n1',
#            '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']

virus = list(input('Enter that hacker\'s name: ').lower())

# ==================== OPTION 1. USING LIST ===============================


# def Search_Virus(list_to_search, name):  # Searching for Anton in fridge name
#     for i in range(len(list_to_search)):  # Going through all strings in the list of fridges
#         # Each string in the list of fridges converting to a list
#         word = list(list_to_search[i])
#         for j in name:                   # Looking for each letter of the name in each string
#             if j in word:
#                 found = True
#                 del word[:word.index(j)+1]
#             else:
#                 found = False
#                 break
#         if found:
#             print(i+1, end=' ')


# Search_Virus(fridges, virus)

# ==================== OPTION 2. USING STRING ===============================
# def Search_Virus(list_to_search, name):  # Searching for Anton in fridge name
#     for fridge in list_to_search:  # Going through all strings in the list of fridges
#         fr_mod, count = fridge, 0
#         for j in name:                   # Looking for each letter of the name in each string
#             if fr_mod.find(j) > -1:
#                 fr_mod = fr_mod[fr_mod.find(j):]
#                 count += 1
#                 if count == len(virus):
#                     print(list_to_search.index(fridge)+1, end=' ')
#             else:
#                 break


# Search_Virus(fridges, virus)

# ==================== OPTION 3. ===========================================


def Search_Virus(list_to_search, name):
    result = []  # Resulting list to where found elements will be put
    count = 0
    for i in name:  # For each letter of virus name
        for j in range(count, len(list_to_search)):  # For
            count += 1
            if i == list_to_search[j]:
                result.append(i)
                break
    if result == list(name):
        return True
    else:
        return False


for i in range(len(fridges)):
    if Search_Virus(fridges[i], virus):
        print(i+1, end=' ')

# ==================== OPTION 4. ===========================================
for i in range(int(input())):
    s, virus, x = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break
