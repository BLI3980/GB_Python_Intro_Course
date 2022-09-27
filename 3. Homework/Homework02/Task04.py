
pos1 = int(input('Enter position #1 value: '))
pos2 = int(input('Enter position #2 value:'))
n = int(input('Enter the size of the list: '))
l = []
for i in range(-n, n+1):
    l.append(i)

print(l)

print(l[pos1-1]*l[pos2-1])
