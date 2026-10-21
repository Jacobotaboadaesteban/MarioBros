import pyxel
# We create the function crab class
class Flies:
    def __init__(self, x: float, y: float, xd: float, ct: float):
        self.x = x
        self.y = y
        self.dibujo = (0, 16, 56, 16, 16, 0)
        self.xd = xd
        self.yd = 0
        self.lives = 1
        self.ct = ct
        self.inAir = False
        self.inFloor = True
        self.down = False
        self.angry = False


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
        if self.down == False:
            # we create the crab animation according to its direction and lives.
            if self.xd > 0:
                self.dibujo = (self.dibujo[0], 16 + 16 * (pyxel.frame_count % 3),
                           self.dibujo[2], -16, self.dibujo[4], self.dibujo[5])
            elif self.xd < 0:
                self.dibujo = (self.dibujo[0], 16 + 16 * (pyxel.frame_count % 3),
                           self.dibujo[2], 16, self.dibujo[4], self.dibujo[5])
            if self.x > 364:
                self.x = 0
            if self.x < 0:
                self.x = 364
            if self.inFloor:
                self.fly()

            self.y += self.yd
            self.x += self.xd
            self.lives = 1

    # They change direction:
    def turn(self):
        self.xd = -self.xd

    # Function which will be used when mario hits them
    def jump(self):
        self.xd = 0
        self.dibujo = (0, 80, 56, 16, 16, 0)

    # We also define the fly platform
    def fly(self):
        self.yd = -5
        self.inAir = True
        self.inFloor = False

    # We also define another function which will be used after a time without
    def angryEnemy(self):
        self.down = False
        self.xd = 2
        self.angry = True