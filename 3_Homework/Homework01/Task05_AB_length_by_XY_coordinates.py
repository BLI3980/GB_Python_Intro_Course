# Task: Coordinates of points A and B are entered by user.
# Create a program which calculates the length of AB segment by given coordinates

x1 = int(input('Enter X coordinate for point A: '))
y1 = int(input('Enter Y coordinate for point A: '))
x2 = int(input('Enter X coordinate for point B: '))
y2 = int(input('Enter Y coordinate for point B: '))

ab = round((abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5, 2)

print(f'The length of AB segment is equal to {ab}')
