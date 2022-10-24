# Объявите анонимную (лямбда) функцию для определения вхождения в переданную
# ей строку фрагмента "plr". То есть, функция должна возвращать True,
# если такой фрагмент присутствует в строке и False - в противном случае.

# ============================================
def removePLR(x): return x.count("plr") > 0


inputStr = input("Enter string:\r\n")
print(removePLR(inputStr))
# ============================================
print(lambda x: x.count('plr') > 0)

# ============================================
print((lambda x: 'ra' in x)(input()))

# ============================================
contains = lambda s, sample='ra': sample in s
s = input()
print(contains(s))
