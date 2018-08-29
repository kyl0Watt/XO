#!/usr/bin/env python3

import random

f_player = 'X'
s_player = 'O'
move_mark = '+'
before_mark = ' '

game_field = [' '] * 9  # 3 * 3 field
current_position = 4
game_field[current_position] = move_mark  #start position

MOVE = {'w': -3,
        's': 3,
        'd': 1,
        'a': -1}


def check_win(game_field):
    """Check field to win"""
    if (game_field[0] != ' ') and (game_field[0] == game_field[1] == game_field[2]):
        return game_field[0]
    elif (game_field[3] != ' ') and (game_field[3] == game_field[4] == game_field[5]):
        return game_field[3]
    elif (game_field[6] != ' ') and (game_field[6] == game_field[7] == game_field[8]):
        return game_field[6]

    elif (game_field[0] != ' ') and (game_field[0] == game_field[3] == game_field[6]):
        return game_field[0]
    elif (game_field[1] != ' ') and (game_field[1] == game_field[4] == game_field[7]):
        return game_field[1]
    elif (game_field[2] != ' ') and (game_field[2] == game_field[5] == game_field[8]):
        return game_field[2]

    elif (game_field[0] != ' ') and (game_field[0] == game_field[4] == game_field[8]):
        return game_field[0]
    elif (game_field[2] != ' ') and (game_field[2] == game_field[4] == game_field[6]):
        return game_field[2]
    elif ' ' not in game_field:
        return 'NoOne'
    else:
        return False


def print_field(game_field):
    """print game field"""
    print('/n',
          '''
          _____________
          | {} | {} | {} |
          | {} | {} | {} |
          | {} | {} | {} |
          _____________\n
          '''.format(game_field[0], game_field[1], game_field[2],
                     game_field[3], game_field[4], game_field[5],
                     game_field[6], game_field[7], game_field[8]))


def user_input():
    """receive user input and return move key or confirm choice"""
    key = input('Move position or press y to do turn: ')
    if key == 'w':
        return key
    elif key == 's':
        return key
    elif key == 'd':
        return key
    elif key == 'a':
        return key
    elif key == 'y':
        return key
    elif key == 'h':
        print('There is no help yet')
    else:
        print('Need help? Press "h"')
    return user_input()


def move(game_field, key):
    """Move move_mark"""
    if (key == 'w' or 's' or 'a' or 'd') and (0 <= (current_position + MOVE[key]) <= 8):
        l_before_mark = game_field[current_position+MOVE[key]]
        game_field[current_position + MOVE[key]] = move_mark
        return game_field, l_before_mark
    elif (key == 'y') and (game_field[current_position] == ' '):
        game_field[current_position] = f_player
        return game_field, False
    else:
        print('\nWrong move? try again\n')
    return False  # return game field and before_mark


def ai_input(game_field):
    """AI move"""
    while True:
        r = random.choice(range(0, 9))
        if game_field[r] == ' ':
            game_field[r] = s_player
            break
        else:
            continue


def main():
    """Main game function"""
    print("Move mark '+' by pressing 'w' 'a' 's' 'd' and 'Enter'")
    print_field(game_field)

    while True:
        if check_win(game_field) == f_player:
            print('Human WIN!!!! ' * 5)
            break
        elif check_win(game_field) == s_player:
            print('AI WIN!!!!! ' * 5)
            break
        elif check_win(game_field) == 'NoOne':
            print('GAME OVER!!! NO ONE WIN ' * 8)
            break
        key = user_input()
        move(game_field, key)
        check_win(game_field)
        print_field(game_field)
        print('*'*15, 'AI turn:\n')
        ai_input(game_field)
        check_win(game_field)
        print_field(game_field)


if __name__ == '__main__':
    main()
