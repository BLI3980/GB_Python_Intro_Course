# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример: *
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# ================== OPTION 1 ============================
# n = int(input("Enter a natural number: "))

# element = 1

# for i in range(1, n+1):
#     element = 3 * i + 1
#     print(i, ":", element, ",", end=" ")

# ================== OPTION 2 ============================
# x = int(input('введите число: '))
# dic = {}
# for i in range(1, x+1):
#     dic[i] = 3 * i + 1

# print(dic)

# ================== OPTION 3 ============================
def PrintList(list_):
    for i in range(len(list_)):
        print(f'{i+1}: {list_[i]}', end=' ')


n = int(input('Введите число: '))
list_ = []

for i in range(1, n+1):
    list_.append(3*i+1)

PrintList(list_)
