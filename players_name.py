class IncorrectName(Exception):
    pass


class PlayersName:
    def __init__(self):
        self.name = ''

    def __str__(self):
        res = ''
        res += ''.join(self.name)
        return res

    def name_error(self, player_name):
        is_ok = True
        try:
            player_name = int(player_name)
            if player_name == 1:
                self.name = 'X'
            elif player_name == 2:
                self.name = 'O'
            else:
                raise IncorrectName
        except ValueError:
            print('You should enter numbers!')
            is_ok = False
        except IncorrectName:
            print('You should enter 1 or 2!')
            is_ok = False
        finally:
            return is_ok

    def correct_name(self):
        input_name = input()
        while not self.name_error(input_name):
            input_name = input()

    def change_player(self):
        if self.name == 'X':
            self.name = 'O'
        elif self.name == 'O':
            self.name = 'X'
