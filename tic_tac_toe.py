value = '_________'
lst = []
for i in range(len(value)):
    lst.append(value[i])

str_1 = lst[:3]
str_2 = lst[3:6]
str_3 = lst[6:9]

field = [str_1, str_2, str_3]
col_1 = []
col_2 = []
col_3 = []

di_1 = []
di_2 = []

for element in range(len(field)):
    for index in range(len(field)):
        if index == 0:
            col_1.append(field[element][index])
        elif index == 1:
            col_2.append(field[element][index])
        elif index == 2:
            col_3.append(field[element][index])
for element in range(len(field)):
    for index in range(len(field)):
        if element == index:
            di_1.append(field[element][index])
for element in range(len(field)):
    for index in range(len(field)):
        if index == (len(field) - element - 1):
            di_2.append(field[element][index])

print('-' * 9,
      '| ' + ' '.join(str_1) + ' |',
      '| ' + ' '.join(str_2) + ' |',
      '| ' + ' '.join(str_3) + ' |',
      '-' * 9, sep='\n')


class IncorrectCoord(Exception):
    pass


class FieldOccupiedError(Exception):
    pass


def change_col(x, y, name):
    if y == 0:
        col_1[x] = name
    elif y == 1:
        col_2[x] = name
    elif y == 2:
        col_3[x] = name
    return col_1, col_2, col_3


def change_di(x, y, name):
    if x == 0:
        if y == 0:
            di_1[x] = name
        if y == 2:
            di_2[x] = name
    elif x == 1 and y == 1:
        di_1[x] = name
        di_2[x] = name
    elif x == 2:
        if y == 0:
            di_2[x] = name
        if y == 2:
            di_1[x] = name
    return di_1, di_2


def check_condition(name):
    a = 0
    while a == 0:
        print(f'{name}, input coordinate from 1 to 3: ')
        try:
            coord = str(input())
            coord = list(map(int, coord.split()))
            a = len_coord(coord[0], coord[1], name)
        except ValueError:
            print(name, 'you should enter numbers!')
        except (IndexError, TypeError):
            print(name, "coordinates should be from 1 to 3!")


def len_coord(x, y, name):
    x = x - 1
    y = y - 1
    a = 0
    try:
        if x >= 3 or y >= 3 or x < 0 or y < 0:
            raise IncorrectCoord
        elif field[x][y] == 'X' or field[x][y] == 'O':
            raise FieldOccupiedError
        else:
            new_field = numbers_field(x, y, name)
            change_col(x, y, name)
            change_di(x, y, name)
    except IncorrectCoord:
        print(name, "coordinates should be from 1 to 3!")
    except FieldOccupiedError:
        print(name, "this cell is occupied! Choose another one!")
    # except IndexError:
    #     print(name, "here3 Coordinates should be from 1 to 3!")
    else:
        a = 1
    return a


def numbers_field(x, y, name):
    try:
        if x == 0:
            str_1[y] = name
        elif x == 1:
            str_2[y] = name
        elif x == 2:
            str_3[y] = name
        new_field = [str_1, str_2, str_3]
        print('-' * 9,
              '| ' + ' '.join(new_field[0]) + ' |',
              '| ' + ' '.join(new_field[1]) + ' |',
              '| ' + ' '.join(new_field[2]) + ' |',
              '-' * 9, sep='\n')
        return new_field
    except TypeError:
        print(name, "coordinates should be from 1 to 3!")


all_ = [str_1, str_2, str_3, col_1, col_2, col_3, di_1, di_2]


def who_wins(count_win):
    for k in all_:
        if k == ['X', 'X', 'X']:
            count_win += 2
        elif k == ['O', 'O', 'O']:
            count_win += 3
    return count_win


win = 0
cnt_x = 0
cnt_o = 0
cnt_ = 9

move = 0
# a = 0

while cnt_ > 0:
    block = who_wins(win)
    if block == 0:
        if move % 2 == 0:
            check_condition('X')
            move += 1
            cnt_x += 1
            cnt_ -= 1
        elif move % 2 == 1:
            check_condition('O')
            move += 1
            cnt_o += 1
            cnt_ -= 1
    elif block == 2 or block == 4:
        print('X wins')
        break
    elif block == 3 or block == 6:
        print('O wins')
        break
    elif block == 5:
        print('Impossible')
        break
else:
    block = who_wins(win)
    if block == 2 or block == 4:
        print('X wins! Congratulations')
    elif block == 3 or block == 6:
        print('O wins! Congratulations!')
    elif block == 5:
        print('Impossible')
    else:
        print('Draw')





