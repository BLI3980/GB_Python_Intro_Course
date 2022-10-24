# Task: Create a program for a Candy game:
# Game conditions: There is N amount of candies on the table. The player making
# the first move is selected by the draw. In one move a player can take from the
# desk from 1 to K candies, inclusive. Whoever takes the last candy wins the
# game and takes all candies of the opponent.

import os
from random import *
import time
os.system('cls' if os.name == 'nt' else 'clear')

start_amnt = randint(100, 500)
take_max = 28

# ================ Rules Description ========================


def Rules():
    print(f'''
Rules:
There are {start_amnt} candies on the table.
The player making the first move is selected by the draw.
In one move a player can take from the desk from 1 to {take_max}
candies, inclusive. Whoever takes the last candy wins the
game and takes all candies of the opponent.\n''')


# ================ Player selection =========================
print('Do you want to play with:\n - 1. a human (press 1)\n - 2. bot (press 2)\n - 3. AI (press 3): ')
mode = int(input('Make your choice: '))
os.system('cls' if os.name == 'nt' else 'clear')
if mode != 1:
    player1 = input('Enter the name of the human: ')
    player2 = input('Enter the name of the bot/AI: ')
else:
    player1 = input('Enter the name of the first player: ')
    player2 = input('Enter the name of the second player: ')
os.system('cls' if os.name == 'nt' else 'clear')
# player1 = 'Player A'
# player2 = 'Player B'

# ================ First move ===============================
move = int(choice([-1, 1]))


def FirstMove(pl1: str, pl2: str):

    if move == 1:
        print(
            f'By random choice \033[31m{pl1}\033[0m is selected to take the first move.\n')
    else:
        print(
            f'By random choice \033[32m{pl2}\033[0m is selected to take the first move.\n')


# ================= Suggest the move ========================


def Suggest(pl1: str, pl2: str, amount: int, turn: int):
    print(f'There are {amount} candies are on the table. ')
    if turn == 1:
        if amount < 28:
            print(
                f'\033[31m{pl1}\033[0m, take [1 .. \033[31m{amount}\033[0m] candies: ', end='')
        else:
            print(
                f'\033[31m{pl1}\033[0m, take [1 .. {take_max}] candies: ', end='')
    else:
        if amount < 28:
            print(
                f'\033[32m{pl2}\033[0m, take [1 .. \033[31m{amount}\033[0m]] candies: ', end='')
        else:
            print(
                f'\033[32m{pl2}\033[0m, take [1 .. {take_max}] candies: ', end='')

# ================= Exceptions ===============================


def CheckInput(amount_left):
    input_num = input()
    while not input_num.isdigit():
        input_num = input('Wrong entry. Please try again: ')
    max_take = min(amount_left, take_max)
    if 0 < int(input_num) <= max_take:
        return int(input_num)
    else:
        print('You cannot take this amount of candies.')
        print(
            f'Please take [\033[31m1 .. {max_take}\033[0m] candies: ', end='')
        return CheckInput(amount_left)


# ================= Game =====================================


def Game(pl1: str, pl2: str):
    left = start_amnt
    turn = move
    while left > 0:
        if mode == 1:
            Suggest(player1, player2, left, turn)
            taken = CheckInput(left)
        elif mode == 2:
            if turn == 1:
                Suggest(player1, player2, left, turn)
                taken = CheckInput(left)
            else:
                taken = randint(1, take_max)
                # time.sleep(0.5)
                print(f'There are {left} candies are on the table. ')
                print(f'\033[32m{pl2}\033[0m has taken {taken} candies.')
                time.sleep(0.5)
        elif mode == 3:
            if turn == 1:
                Suggest(player1, player2, left, turn)
                taken = CheckInput(left)
            else:
                taken = left - left // (take_max+1) * (take_max+1)
                if 1 > taken or taken > take_max:
                    taken = randint(1, take_max)
                # time.sleep(0.5)
                print(f'There are {left} candies are on the table. ')
                print(f'\033[32m{pl2}\033[0m has taken {taken} candies.')
                time.sleep(0.5)
        left = left - taken
        turn = -turn
    else:
        if turn == 1 and left == 0:
            print(f'\n\033[32m{pl2}\033[0m has WON!!!.\n')
        else:
            print(f'\n\033[31m{pl1}\033[0m has WON!!!.\n')


# ================= Initialize ===============================
Rules()
FirstMove(player1, player2)
Game(player1, player2)
