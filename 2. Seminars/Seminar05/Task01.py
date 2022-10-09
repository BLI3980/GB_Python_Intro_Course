# Task: Найти НОД (Наибольший общие делитель)



def NOD(a, b):
    if a < b:
        a, b = b, a
    while True:
        res = a % b
        if res == 0:
            return b
        else:
            a, b = b, res


# def NOD(a: int, b: int):
#     if b > a:
#         a, b = b, a
#     while True:
#         rem = a % b
#         if (rem == 0):
#             return b
#         else:
#             a = b
#             b = rem

a = int(input("Enter a:\r\n"))
b = int(input("Enter b:\r\n"))

print(NOD(a, b))
# ============================================================
a = 20
b = 58

if a < b:
    a, b = b, a

while b != 0:
    a, b = b, a % b

print(a)

# ============================================================
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)
