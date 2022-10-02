# Task: Create a program which converts decimal number to binary.
# Examples: 45 -> 101101; 3 -> 11; 2 -> 10

dec = int(input('Enter a decimal number: '))


def Dec_to_Bin(num):
    bin = str()
    while num != 0:
        bin = str(num % 2) + bin
        num //= 2
    return bin


print(f'Decimal number {dec} in binary system is: {Dec_to_Bin(dec)}')
