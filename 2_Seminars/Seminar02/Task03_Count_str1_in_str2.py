# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# ========== OPTION 1 ===========================

s = input('Введите первую строку: ')
s_1 = input('Введите вторую строку: ')

# if len(s) > len(s_1):
#     s, s_1 = s_1, s

count = 0
for i in s:
    for j in s_1:
        if i == j:
            print(f' i={i}, j={j}')
            count += 1

print(count)

# ========== OPTION 2 ===========================

# a = input('Enter a string 1: ')
# b = input('Enter a string 2: ')

# # Counts only how many times the entire string b appears in string a
# print(a.count(b))

# ========== OPTION 3 ===========================

# word1 = input('Введите слово: ')
# word2 = input('Введите второе слово: ')

# # Counts only how many times the entire string b appears in string a
# print(f'Слово "{word2}" встречается {word1.count(word2)} раз.')

# ========== OPTION 4 ===========================

st1 = input("Введите 1 строку: ")
st2 = input("Введите 2 строку: ")

total = 0
for i in range(len(st1)):
    for j in range(len(st2)):
        if st1[i] == st2[j]:
            print(f' i={i}, j={j}')
            total += 1
print(total)
