class IncorrectCoord(Exception):
    pass


class FieldOccupiedError(Exception):
    pass


class MakeField:
    def __init__(self):
        self.value = [['_' for _ in range(3)] for __ in range(3)]
        self.column_1 = ['_' for _ in range(3)]
        self.column_2 = ['_' for _ in range(3)]
        self.column_3 = ['_' for _ in range(3)]
        self.di_1 = ['_' for _ in range(3)]
        self.di_2 = ['_' for _ in range(3)]
        self.all = [['_' for _ in range(3)] for __ in range(8)]

    def __str__(self):
        res = '-' * 9 + '\n'
        for line in self.value:
            res += '| ' + ' '.join(line) + ' |\n'
        res += '-' * 9
        return res

    def column_di(self):
        self.column_1 = [self.value[0][0], self.value[1][0], self.value[2][0]]
        self.column_2 = [self.value[0][1], self.value[1][1], self.value[2][1]]
        self.column_3 = [self.value[0][2], self.value[1][2], self.value[2][2]]
        self.di_1 = [self.value[0][0], self.value[1][1], self.value[2][2]]
        self.di_2 = [self.value[0][2], self.value[1][1], self.value[2][0]]
        self.all = [self.value[0], self.value[1], self.value[2],
                    self.column_1, self.column_2, self.column_3, self.di_1, self.di_2]

    def try_error(self, coord, name_player):
        is_ok = True
        try:
            coord = list(map(int, coord.split()))
            x = coord[0] - 1
            y = coord[1] - 1
            if x >= 3 or y >= 3 or x < 0 or y < 0:
                raise IncorrectCoord
            elif self.value[x][y] == 'X' or self.value[x][y] == 'O':
                raise FieldOccupiedError
        except ValueError:
            print(f'{name_player}, you should enter numbers! wrong_1')
            is_ok = False
        except (IndexError, TypeError):
            print(f'{name_player}, you should enter two coordinates! wrong_2')
            is_ok = False
        except IncorrectCoord:
            print(f'{name_player}, coordinates should be from 1 to 3! wrong_3')
            is_ok = False
        except FieldOccupiedError:
            print(f'{name_player}, this cell is occupied! Choose another one! wrong_4')
            is_ok = False
        finally:
            return is_ok

    def new_move(self, name_player):
        print(f'{name_player}, input coordination from 1 to 3:')
        input_coord = str(input())
        while not self.try_error(input_coord, name_player):
            input_coord = str(input())
        coord = list(map(int, input_coord.split()))
        x = coord[0] - 1
        y = coord[1] - 1
        self.value[x][y] = str(name_player)
        self.column_di()
        a = self.who_win()
        return a

    def who_win(self):
        wins = 0
        for row in self.all:
            if row == ['X', 'X', 'X']:
                wins = 2
            elif row == ['O', 'O', 'O']:
                wins = 3
        return wins
