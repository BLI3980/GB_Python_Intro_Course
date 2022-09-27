
x = int(input('введите число: '))
dic = {}
sum = 0
for i in range(1, x+1):
    dic[i] = int(round((1 + 1/i) ** i, 0))
    sum += dic[i]

print(dic, sum)
