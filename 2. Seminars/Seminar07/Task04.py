#

# l.sort(key= lambda x: len(x), reverse=True)
# print(*l)


s = sorted(input().split(), key=lambda x: len(x)[::-1]
print(*s)
