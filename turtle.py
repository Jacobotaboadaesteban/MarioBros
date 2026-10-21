import pyxel


# We create the turtle class:
class Turtle:
    def __init__(self, x: float, y: float, xd: float, ct: float):
        self.x = x
        self.y = y
        self.dibujo = (0, 0, 24, 16, 16, 0)
        self.xd = xd
        self.yd = 0
        self.inAir = False
        self.inFloor = True
        self.down = False
        self.lives = 1
        self.angry = False
        self.ct = ct

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def updateEnemy(self):
        # we create the turtle animation according to its direction
            if self.angry == False:
                if self.xd > 0:
                    self.dibujo = (0, 0 + 16 * (pyxel.frame_count % 3), 24, -16, 16, 0)
                elif self.xd < 0:
                    self.dibujo = (0, 0 + 16 * (pyxel.frame_count % 3), 24, 16, 16, 0)

            if self.angry == True:
                if self.xd > 0:
                    self.dibujo = (0, 0 + 16 * (pyxel.frame_count % 3), 128, -16,
                               16, 0)
                elif self.xd < 0:
                    self.dibujo = (0, 0 + 16 * (pyxel.frame_count % 3), 128,
                                   16, 16, 0)

            if self.x > 364:
                self.x = 0
                self.y = self.y - 20
                self.yd = -2
            # if not the turtle falls when goes from one side to the other
            if self.x < 0:
                self.x = 364
                self.y = self.y - 20
                self.yd = -2

            self.x += self.xd
            self.y += self.yd

    # They change direction:
    def turn(self):
        self.xd = -self.xd

    # Function which will be used when mario hits them
    def jump(self):
        self.xd = 0
        if self.angry == False:
            self.dibujo = (0, 112, 24, 16, 16, 0)
        if self.angry == True:
            self.dibujo = (0, 112, 128, 16, 16, 0)

    # We also define another function which will be used after a time without
    # being touched and being down
    def angryEnemy(self):
        self.down = False
        self.xd = 2
        self.angry = True
