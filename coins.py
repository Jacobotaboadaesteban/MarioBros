import pyxel
#We create a class for the coins with a position and a direction which will
#be used to change its movement if it collides with something
class Coin:
    def __init__(self, x: float, y: float, xd: float):
        self.x = x
        self.y = y
        self.xd = xd
        self.yd = 0
        self.inAir = True
        self.yx = 0
        self.dibujo = (0, 208, 212, 8, 10,0)

    # The function coin update is used to define its draw when it's moving
    # and to make it appear on the other side of the screen when it passes
    # from one side to another
    def coinupdate(self):
        self.x += self.xd
        if self.x > 356:
            self.x = 0
        if self.x < 0:
            self.x = 356
        if self.xd > 0:
            self.dibujo = (0, 0 + 8 * (pyxel.frame_count%5), 208, -8, 16, 0)
        elif self.xd < 0:
            self.dibujo = (0, 0 + 8 * (pyxel.frame_count%5), 208, 8, 16, 0)

    # The turn function will be used all along the code when it collides
    def turn(self):
        self.xd = -self.xd
