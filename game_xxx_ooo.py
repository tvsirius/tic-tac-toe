import random
import itertools

from board import Board


print('HELLO! Xx0o game!! Terminal ver ')

# dimension=int(input('Enter board dimentions:'))

dimension =3

myboard = Board(dimension, 2)

# myboard.show()

print(myboard)


total_players = 2


players = itertools.cycle(range(1, total_players + 1))

comp_pl = int(input('Enter comp player num(1 or 2): '))

if comp_pl not in [1, 2]:
    exit(0)

while not myboard.checkwin_all_players(total_players):
    if myboard.full():
        print('Game Over without winner!')
        break
    nextpl = next(players)
    print(f'Player {nextpl} ({Board.player_chars[nextpl]}) move ')
    if nextpl == comp_pl:
        comp_vars = myboard.computer_move(comp_pl)

        x, y = random.choice(comp_vars)
        myboard[x][y] = comp_pl
    else:
        while not myboard.inputmove(nextpl):
            pass
    myboard.show()


myboard.display_winners()

myboard.show()