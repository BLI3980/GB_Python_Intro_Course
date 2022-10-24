# Task: Create a program which takes as an input X and Y coordinates of a point
# and returns the quadrant of this point. X ≠ 0 and Y ≠ 0.
x = int(input('Enter X coordinate of a point: '))
y = int(input('Enter Y coordinate of a point: '))

if x == 0 or y == 0:
    print('Please use coordinates that are not equal to zero.')
elif x > 0:
    if y > 0:
        print('The point is situated in the 1st quadrant.')
    else:
        print('The point is situated in the 4th quadrant.')
else:
    if y > 0:
        print('The point is situated in the 2nd quadrant.')
    else:
        print('The point is situated in the 3rd quadrant.')
