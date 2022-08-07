from field import MakeField
from players_name import PlayersName


welcome = ("""Hello! 
Choose a player: X or O. 
Enter 1 if you want to play for X. 
Enter 2 if you want to play for O.""")

print(welcome)

name = PlayersName()
name.correct_name()
print(f'{name}, your move will be the first')

field = MakeField()
print(field)

a = 0
cnt_motion = 1
while a == 0 and cnt_motion != 10:
    if cnt_motion % 2 == 1:
        a = field.new_move(name)
        print(field)
        cnt_motion += 1
        name.change_player()
    elif cnt_motion % 2 == 0:
        a = field.new_move(name)
        print(field)
        cnt_motion += 1
        name.change_player()

if a == 2:
    print('X wins!')
elif a == 3:
    print('O wins!')
elif cnt_motion == 10:
    print('Draw')
