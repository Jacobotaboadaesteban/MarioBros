#In order to create the pow, we make a new class named pow wich will have
#a position x, y, a draw and some lives.
class Pow:
    def __init__(self, x: int, y: int, lives: float):
        self.x = x
        self.y = y
        self.dibujo = (0, 136, 176, 16, 16)
        self.lives = lives


#The pow will have a funtion called change which will make the draw change
#when it is hit. The effects of hittig the pow will be defined in the main
    # program
    def powChange(self):
        self.lives -= 1
        if self.lives == 2:
            self.dibujo = (0, 152, 176, 16, 16)
        if self.lives == 1:
            self.dibujo = (0, 168, 176, 16, 16)
        if self.lives == 0:
            self.dibujo = (0, -100, -100, 0, 0)