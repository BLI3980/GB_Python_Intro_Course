# Task: На вход программы поступает список наименований рек, записанных в одну
# строку через пробел. Необходимо отсортировать этот список в порядке убывания
# длин названий. Результат вывести в одну строчку через пробел
# Sample input:
# Лена Енисей Волга Дон
# Sample output:
# Енисей Волга Лена Дон

in_str = 'Лена Енисей Волга Дон'
print(in_str)

# ========================== OPTION 1 =======================================
in_str.sort(key=lambda x: len(x), reverse=True)
print(*in_str)

# ========================== OPTION 2 =======================================
# With sorted() original list is unchanged
out_str1 = sorted(in_str.split(), key=lambda x: len(x), reverse=True)
out_str2 = sorted(in_str.split(), key=lambda x: len(x))[::-1]

# print each element of the list separated by space
print(*out_str1)
print(*out_str2)
