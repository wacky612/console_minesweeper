class Square:
    def __init__(self):
        self.is_opened = False
        self.is_mined = False
        self.is_flaged = False
        self.number_of_surrounding_mines = 0

    def open(self):
        if self.is_opened:
            return -2
        else:
            self.is_opened = True
            if self.is_mined:
                return -1
            else:
                return self.number_of_surrounding_mines

    def install_mine(self):
        if self.is_mined:
            return False
        else:
            self.is_mined = True
            return True

    def increment_number_of_surrounding_mines(self):
        self.number_of_surrounding_mines += 1

    def toggle_flag(self):
        self.is_flaged = not self.is_flaged

    def render(self):
        #if not self.is_opened:
        #    return '.'

        if self.is_mined:
            return '*'

        if self.number_of_surrounding_mines == 0:
            return ' '

        return str(self.number_of_surrounding_mines)
