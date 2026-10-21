# We use a new class for tubes just giving them the value x, y and its draw,
# which will be defined in board
class Tubes:
    def __init__(self, x: int, y: int, dibujo: tuple):
        self.x = x
        self.y = y
        self.dibujo = dibujo