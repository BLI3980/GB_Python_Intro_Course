# Task: Create a program, which shows the range of X and Y coordinates
# of a point, based on it's quadrant

quadrant = int(input('Enter the quadrant of a point: '))

if 0 < quadrant < 5:
    if quadrant <= 2:
        if quadrant == 1:
            print('X > 0 and Y > 0')
        else:
            print('X < 0 and Y > 0')
    else:
        if quadrant == 4:
            print('X > 0 and Y < 0')
        else:
            print('X < 0 and Y < 0')
else:
    print('The number must be between 1 and 4, inclusive. Try again')


