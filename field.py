import square
import random
import itertools

class Field:
    def __init__(self, width, height, number_of_mines):
        self.squares = []
        self.width = width
        self.height = height
        
        for x in range(width):
            self.squares.append([])
            for y in range(height):
                self.squares[x].append(square.Square())

        for i in range(number_of_mines):
            while True:
                if self.squares[random.randrange(width)][random.randrange(height)].install_mine():
                    break

        for x, y in itertools.product(range(width), range(height)):
            if self.squares[x][y].is_mined:
                for x2, y2 in itertools.product(range(max(0, x-1), min(width, x+2)),
                                                range(max(0, y-1), min(height, y+2))):
                    self.squares[x2][y2].increment_number_of_surrounding_mines()
                        

    def open(self, x, y):
        result = self.squares[x][y].open()
        if result == 0:
            for x2, y2 in itertools.product(range(max(0, x-1), min(self.width, x+2)),
                                            range(max(0, y-1), min(self.height, y+2))):
                self.open(x2, y2)

        if result == -1:
            return False
        else:
            return True

    def render(self):
        for y in range(self.height):
            buffer = ''
            for x in range(self.width):
                buffer += self.squares[x][y].render()
            print(buffer)

if __name__ == '__main__':
    field = Field(15,10,20)
    field.open(3,3)
    field.open(7,9)
    field.render()
