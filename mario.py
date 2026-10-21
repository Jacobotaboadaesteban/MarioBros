import pyxel
#The mario class
class Mario:
    def __init__(self, x: float, y: float, lives: int):
        self.x = x
        self.y = y
        self.dibujo = (0, 0, 0, 16, 24, 0)
        self.xd = 0
        self.yd = 0
        self.inAir = False
        self.inFloor = False
        self.lives = lives
        self.Alive = True
        self.invulnerable = 0

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: int):
        if y > 186:
            self.__y = 186
        else:
            self.__y = y


    # it's movement will be defined in this function
    def mario_movement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.xd = 3
            if self.xd > 0:
                self.x += self.xd
        elif pyxel.btn(pyxel.KEY_LEFT):
                self.xd = -3
                if self.xd < 0:
                    self.x += self.xd
                if self.x < 0:
                    self.x = 356
        else:
            self.xd = 0

        if self.x > 356:
                self.x = 0
        if self.xd == 0:
            self.dibujo = (self.dibujo[0], 0, self.dibujo[2], self.dibujo[3],
                           self.dibujo[4], self.dibujo[5])

        else:
            self.dibujo = (self.dibujo[0], 16 + 16 * (pyxel.frame_count % 3),
                       self.dibujo[2], 16, self.dibujo[4], self.dibujo[5])

        if self.xd < 0:
            self.dibujo = (self.dibujo[0], self.dibujo[1], self.dibujo[2], -16,
                           self.dibujo[4], self.dibujo[5])


    def mariohitted(self):
        if self.invulnerable > 0:
            return
        self.y = 0
        self.x = 179
        self.lives -= 1
        self.Alive = False
        self.invulnerable = 60
        self.inAir = True
        self.inFloor = False
        self.yd = 0


    def jump(self):
        self.yd = -12
        self.inAir = True
        self.inFloor = False
