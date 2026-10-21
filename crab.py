import pyxel
# We create the function crab class
class Crab:
    def __init__(self, x: float, y: float, xd: float, ct: float):
        self.x = x
        self.y = y
        self.dibujo = (0, 0, 40, 16, 16, 0)
        self.xd = xd
        self.yd = 0
        self.lives = 2
        self.ct = ct
        self.angry = False
        self.inAir = False
        self.inFloor = True
        self.down = False

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
        if self.angry == False:
        # we create the crab animation according to its direction and lives.
            if self.lives == 2:
                if self.xd > 0:
                    self.dibujo = (self.dibujo[0], 16 + 16 * (pyxel.frame_count % 3),
                           self.dibujo[2], -16, self.dibujo[4],
                                   self.dibujo[5])
                elif self.xd < 0:
                    self.dibujo = (self.dibujo[0], 16 + 16 * (pyxel.frame_count % 3),
                           self.dibujo[2], 16, self.dibujo[4], self.dibujo[5])
            if self.lives == 1:
                if self.xd > 0:
                    self.xd = 2
                    self.dibujo = (self.dibujo[0], 88 + 16 * (
                            pyxel.frame_count % 3),
                           self.dibujo[2], -16, self.dibujo[4], self.dibujo[5])
                elif self.xd < 0:
                    self.xd = -2
                    self.dibujo = (self.dibujo[0], 88 + 16 * (
                            pyxel.frame_count % 3),
                           self.dibujo[2], 16, self.dibujo[4], self.dibujo[5])
        if self.angry == True:
            self.xd = 2 if self.xd >= 0 else -2
            if self.xd > 0:
                self.dibujo = (self.dibujo[0], 88 + 16 * (
                        pyxel.frame_count % 3),
                               144, -16, self.dibujo[4],
                               self.dibujo[5])
            elif self.xd < 0:
                self.dibujo = (self.dibujo[0], 88 + 16 * (
                        pyxel.frame_count % 3),
                               144, 16, self.dibujo[4],
                               self.dibujo[5])

        if self.x > 364:
             self.x = 0
             self.y = self.y - 10
            # if not the crab falls when goes from one side to the other
        if self.x < 0:
            self.x = 364
            self.y = self.y - 10
        # The direction is converted into position
        self.x += self.xd
        self.y += self.yd

    # They change direction:
    def turn(self):
        self.xd = -self.xd

    # Function which will be used when mario hits them
    def jump(self):
        self.xd = 0
        if self.angry == False:
            self.dibujo = (0, 152, 40, 16, 16, 0)
        if self.angry == True:
            self.dibujo = (0, 152, 128, 16, 16, 0)

    # We also define another function which will be used after a time without
    def angryEnemy(self):
        self.down = False
        self.xd = 2
        self.angry = True

