#!/usr/bin/env python3

import random

f_player = 'X'  # type: str
s_player = 'O'  # type: str
move_mark = '+'  # type: str

game_field = [' '] * 9  # 3 * 3 field
start_position = 4
game_field[start_position] = move_mark  # start position

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
    print('''
          _____________
          | {} | {} | {} |
          | {} | {} | {} |
          | {} | {} | {} |
          _____________
          '''.format(game_field[0], game_field[1], game_field[2],
                     game_field[3], game_field[4], game_field[5],
                     game_field[6], game_field[7], game_field[8]))


def user_input():
    """receive user input and return move key or confirm choice"""
    key = input('Move position or press y to do turn: ')
    if key == 'w' or 's' or 'd' or 'a' or 'y':
        return key
    elif key == 'h':
        print('There is no help yet')
    else:
        print('Need help? Press "h"')
    return user_input()


def move(game_field, key, before_mark, new_position):
    """Move move_mark"""
    if (key in ['w', 'a', 's', 'd']) and (0 <= (new_position + MOVE[key]) <= 8):
        if before_mark:
            game_field[new_position] = before_mark
        before_mark = game_field[new_position+MOVE[key]]
        game_field[new_position + MOVE[key]] = move_mark
        new_position = new_position + MOVE[key]
        return before_mark, new_position
    elif (key == 'y') and (before_mark == ' '):
        game_field[new_position] = f_player
        before_mark = f_player
        return before_mark, new_position
    else:
        print('\nWrong move! try again\n')
    return before_mark, new_position


def ai_input(game_field):  # TODO: AI
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
    print("\nMove mark '+' by pressing 'w' 'a' 's' 'd' and 'Enter'")
    print_field(game_field)
    before_mark = ' '
    new_position = start_position

    while True:
        ch_win = check_win(game_field)
        if ch_win == f_player:
            print('Human WIN!!!!\n' * 5)
            break
        elif ch_win == s_player:
            print('AI WIN!!!!!\n' * 5)
            break
        elif ch_win == 'NoOne':
            print('GAME OVER!!! NO ONE WIN\n' * 8)
            break
        key = user_input()
        before_mark, new_position = move(game_field, key, before_mark, new_position)
        check_win(game_field)
        print_field(game_field)
        if key == 'y':
            print('*' * 15, 'AI turn:\n')
            ai_input(game_field)
            check_win(game_field)
            print_field(game_field)


if __name__ == '__main__':
    main()
