# Task: Create a program for Tic-tak-toe game.

import os
import time
os.system('cls' if os.name == 'nt' else 'clear')


positions = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}


def Table(positions):
    print(f'-+---+---+---+-\n',
          positions.get(1), positions.get(2), positions.get(3),
          '\n-+---+---+---+-\n',
          positions.get(4), positions.get(5), positions.get(6),
          '\n-+---+---+---+-\n',
          positions.get(7), positions.get(8), positions.get(9),
          '\n-+---+---+---+-\n', sep=' | ')


turn = 1


def Call(table, turn):
    os.system('cls' if os.name == 'nt' else 'clear')
    Table(table)
    if turn % 2 != 0:
        call = int(input('Enter a free position where you want to place X: '))
    else:
        call = int(input('Enter a free position where you want to place O: '))
    if table[call] == 'O' or table[call] == 'X':
        print('This position is already taken. Choose another one.')
        time.sleep(1)
        Call(table, turn)
    else:
        if turn % 2 != 0:
            table[call] = 'X'
        else:
            table[call] = 'O'
        turn += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        Table(table)
        count = 0
        check_X = [v for v in table.keys() if table[v] == 'X']
        check_O = [v for v in table.keys() if table[v] == 'O']
        win =  \
            [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
             [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
        for i in win:
            if i == check_X:
                print('Player 1 has WON!!!\n\n')
                return
            elif i == check_O:
                print('Player 2 has WON!!!\n\n')
                return
        for v in table.values():
            if v == 'O' or v == 'X':
                count += 1
            if count == 9:
                time.sleep(0.5)
                print('The draw.\n\n')
                return
        Call(table, turn)


Call(positions, turn)
