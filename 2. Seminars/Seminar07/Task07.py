# ======================================================
# l_value = [23, 63, 2, 81 ,34, 234]
# l_value = filter(lambda x: (9 < x < 100) and (x % 9 == 0),  l_value)
# l_value = map(lambda x: x**2, l_value)
# print(sum(l_value))


# ======================================================
input = list(filter(lambda x: x % 9 == 0, list(range(10, 100))))
input = list(map(lambda x: x**2, input))
input_sum = sum(input)
