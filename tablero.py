import pyxel
from mario import Mario
from brick import Brick
from pow import Pow
from tubes import Tubes
from coins import Coin
from turtle import Turtle
from lifescounter import Lifes
from counter import Ui
from crab import Crab
from flies import Flies


# We start creating the Board class with a width and a length and where all
# the other classes have their attributes given
def hitting(enemy, launch=True):
    if not enemy.down:
        enemy.lives -= 1
        if launch:
            enemy.y -= 20
    elif enemy.down:
        enemy.lives += 1
        if type(enemy) == Turtle or type(enemy) == Crab:
            enemy.y -= 20
        if not enemy.angry:
            enemy.xd = 1
        if enemy.angry:
            enemy.xd = 2

    if enemy.lives == 0:
        enemy.down = True
    else:
        enemy.down = False


class Board:
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

        self.lifescounter = Lifes(80, 10)
        self.mario = Mario(20, 93, 3)
        # We create an empty list in which we will append all the floors
        self.bricks = []
        self.pow = Pow(self.width // 2, 140, 3)
        self.counter = Ui(000000000)
        self.gameOver = False

        for i in range((self.width // 16) + 1):
            self.bricks.append(Brick(i * 16, 210, (0, 120, 176, 16, 16)))

        for i in range(-100, int(((600 // 10) + 1) / 3)):  # Cada for
            self.bricks.append(Brick(i * 7, 160, (0, 0, 224, 8, 8)))

        for i in range(-100, int(((500 // 10) + 1) / 7)):
            self.bricks.append(Brick(i * 7, 115, (0, 0, 224, 8, 8)))

        for i in range(-100, int(((600 // 9) + 1) / 3) - 1):
            self.bricks.append(Brick((i * 7), 40, (0, 0, 224, 8, 8)))

        for i in range(int(((600 // 9) + 1) / 3)):
            self.bricks.append(Brick(363 - (i * 7), 40, (0, 0, 224, 8, 8)))

        for i in range(int(((500 // 10) + 1) / 7) + 1):
            self.bricks.append(Brick(363 - (i * 7), 115, (0, 0, 224, 8, 8)))

        for i in range(int(((600 // 10) + 1) / 3) + 1):
            self.bricks.append(Brick(363 - (i * 7), 160, (0, 0, 224, 8, 8)))

        for i in range(100, 256, 7):
            self.bricks.append(Brick(i, 100, (0, 0, 224, 8, 8)))

        # We can also create the tubes with just 1 function
        self.tube1 = Tubes(306, 0, (0, 0, 176, 50, 32, 0))
        self.tube2 = Tubes(0, 0, (0, 61, 176, 50, 32, 0))
        self.tube3 = Tubes(0, 185, (0, 40, 188, 40, 20, 0))
        self.tube4 = Tubes(316, 185, (0, 32, 188, 40, 20, 0))
        self.tubes = [self.tube1, self.tube2, self.tube3, self.tube4]

        # We create 2 empty lists in which we append the x and y values of each
        # of our floors
        self.floorX = []
        self.floorY = []
        for i in range(len(self.bricks)):
            self.floorX.append(self.bricks[i].x)
            self.floorY.append(self.bricks[i].y)

        # We create also 2 more empty lists in which we will append all the
        # coins and the different kind of enemies
        self.enemies = []
        self.coins = []

        pyxel.init(self.width, self.length, title="Mario Bros", fps=30,
                   display_scale=3)
        pyxel.load("assets/resources.pyxres")
        pyxel.playm(0)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.gameOver:
            if self.mario.invulnerable > 0:
                self.mario.invulnerable -= 1
            # We use the frame count to create the enemies and coins
            # and also for the different levels
            if pyxel.frame_count % 720 == 0 and pyxel.frame_count != 0:
                self.coins.append(Coin(32, 22, 2))
            if pyxel.frame_count % 1750 == 0 and pyxel.frame_count != 0:
                self.coins.append(Coin(306, 22, - 2))
            if pyxel.frame_count % 1000 == 0:
                self.enemies.append(Turtle(306, 22, -1, 1000000))

            if pyxel.frame_count < 1000:
                if pyxel.frame_count % 400 == 0 and pyxel.frame_count != 0:
                    self.enemies.append(Turtle(32, 22, 1, 1000000))
                if pyxel.frame_count % 600 == 0 and pyxel.frame_count != 0:
                    self.enemies.append(Turtle(306, 22, - 1, 1000000))

            if 1000 < pyxel.frame_count < 6000:
                if pyxel.frame_count % 750 == 0:
                    self.enemies.append(Crab(32, 22, 1, 1000000))
                if pyxel.frame_count % 1250 == 0:
                    self.enemies.append(Flies(32, 22, 1, 1000000))
                if pyxel.frame_count % 1800 == 0:
                    self.enemies.append(Flies(306, 22, -2, 1000000))

            if 4000 < pyxel.frame_count < 6000:
                if pyxel.frame_count % 2376 == 0:
                    self.enemies.append(Crab(32, 22, 1, 1000000))
                if pyxel.frame_count % 2800 == 0:
                    self.enemies.append(Flies(32, 22, 1, 1000000))
                if pyxel.frame_count % 4327 == 0:
                    self.enemies.append(Flies(306, 22, -2, 1000000))
                if pyxel.frame_count % 4294 == 0:
                    self.enemies.append(Turtle(306, 22, -2, 1000000))

            # We create some functions in the game as quitting it
            if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()

            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_SPACE):
                if self.mario.inFloor:
                    self.mario.jump()

            previous_mario_y = self.mario.y
            self.mario.mario_movement()
            if self.mario.inAir:
                self.mario.yd += 1
                self.mario.y += self.mario.yd
            else:
                self.mario.yd = 0

            for coin in self.coins[:]:
                coin.coinupdate()
                self.coincollision(coin)
                if coin.inAir:
                    coin.yd += 1
                    coin.y += coin.yd

            self.mariocollision(previous_mario_y)

            if self.pow.lives > 0:
                self.powcollision()

            self.tubestp()
            self.lifeschange()

            for enemy in self.enemies:
                previous_enemy_y = enemy.y
                enemy.updateEnemy()
                if enemy.inAir:
                    enemy.yd += 1
                    enemy.y += enemy.yd
                self.enemiescollision(enemy, previous_enemy_y)

            self.enemy_enemy_collisions()

            if self.mario.xd != 0 or self.mario.yd != 0:
                self.mario.Alive = True

            for enemy in self.enemies:
                if enemy.down:
                    enemy.xd = 0
                    enemy.jump()
                if (enemy.lives == 0 and pyxel.frame_count ==
                        enemy.ct + 100):
                    enemy.down = False
                    enemy.lives += 1
                    enemy.angryEnemy()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(60, 10, str(pyxel.frame_count), 14)
        pyxel.blt(self.lifescounter.x, self.lifescounter.y,
                  *self.lifescounter.dibujo)
        for brick in self.bricks:
            pyxel.blt(brick.x, brick.y, *brick.dibujo)
        pyxel.blt(self.pow.x, self.pow.y, *self.pow.dibujo)
        for tube in self.tubes:
            pyxel.blt(tube.x, tube.y, *tube.dibujo)
        pyxel.blt(self.mario.x, self.mario.y, *self.mario.dibujo)
        for enemy in self.enemies:
            pyxel.blt(enemy.x, enemy.y, *enemy.dibujo)

        for coin in self.coins[:]:
            pyxel.blt(coin.x, coin.y, *coin.dibujo)
        self.counter.drawPoints()
        if pyxel.frame_count < 100:
            pyxel.text(170, 50, str("Stage 1"), 14)
        if 1000 < pyxel.frame_count < 1100:
            pyxel.text(170, 50, str("Stage 2"), 14)
        if 2500 < pyxel.frame_count < 2600:
            pyxel.text(170, 50, str("Stage 3"), 14)
        if 4000 < pyxel.frame_count < 4100:
            pyxel.text(170, 50, str("Stage 4"), 14)

    def powcollision(self):
        if (self.mario.y + 24 // 1 in range(self.pow.y - 10,
                                            self.pow.y + 3) and
                self.mario.x // 1 in range(self.pow.x - 8, self.pow.x + 8)):
            self.mario.inAir = False
            self.mario.inFloor = True
            self.mario.y = self.pow.y - 24
            self.mario.yd = 0
        if (self.mario.y // 1 in range(self.pow.y + 4, self.pow.y + 7) and
                self.mario.x // 1 in range(self.pow.x - 8, self.pow.x + 8)):

            self.mario.inAir = True
            self.mario.yd = 0
            self.pow.powChange()
            for enemy in self.enemies:
                hitting(enemy)

    def coincollision(self, coin):
        # Coins use an 8x10 hitbox. Process only this coin so every coin is
        # moved and collected exactly once per frame.
        if (self.mario.x < coin.x + 8 and self.mario.x + 16 > coin.x and
                self.mario.y < coin.y + 10 and self.mario.y + 24 > coin.y):
            if coin in self.coins:
                self.coins.remove(coin)
                self.addPoints(800)
            return

        for enemy in self.enemies:
            if (coin.x < enemy.x + 16 and coin.x + 8 > enemy.x and
                    coin.y < enemy.y + 16 and coin.y + 10 > enemy.y):
                coin.turn()
                enemy.turn()

        for other in self.coins:
            if other is not coin and (coin.x < other.x + 8 and coin.x + 8 > other.x and
                                      coin.y < other.y + 10 and coin.y + 10 > other.y):
                coin.turn()

        coin.inAir = True
        for floor_x, floor_y in zip(self.floorX, self.floorY):
            floor_width = 16 if floor_y == 210 else 8
            if (coin.x < floor_x + floor_width and coin.x + 8 > floor_x and
                    coin.y + 10 <= floor_y + 2 and coin.y + 10 + coin.yd >= floor_y):
                coin.y = floor_y - 10
                coin.yd = 0
                coin.inAir = False
                break
        if coin.y + 10 >= self.length - 14:
            coin.y = self.length - 24
            coin.yd = 0
            coin.inAir = False

    def enemiescollision(self, entity, previous_y=None):
        if previous_y is None:
            previous_y = entity.y
        previous_bottom = previous_y + 16
        current_bottom = entity.y + 16
        entity.inAir = True
        landed = False
        for floor_x, floor_y in zip(self.floorX, self.floorY):
            floor_width = 16 if floor_y == 210 else 8
            if (entity.x < floor_x + floor_width and entity.x + 16 > floor_x and
                    entity.yd >= 0 and previous_bottom <= floor_y + 2 and
                    current_bottom >= floor_y):
                entity.y = floor_y - 16
                entity.yd = 0
                entity.inAir = False
                landed = True
                if isinstance(entity, Flies):
                    entity.inFloor = True
                break
        if not landed and entity.yd == 0:
            for floor_x, floor_y in zip(self.floorX, self.floorY):
                floor_width = 16 if floor_y == 210 else 8
                if (entity.x < floor_x + floor_width and entity.x + 16 > floor_x and
                        abs(entity.y + 16 - floor_y) <= 1):
                    entity.inAir = False
                    if isinstance(entity, Flies):
                        entity.inFloor = True
                    break
        if entity.y + 16 >= self.length - 14:
            entity.y = self.length - 30
            entity.yd = 0
            entity.inAir = False

    def enemy_enemy_collisions(self):
        """Make overlapping enemies turn away from each other once per frame."""
        for index, first in enumerate(self.enemies):
            for second in self.enemies[index + 1:]:
                overlaps = (first.x < second.x + 16 and first.x + 16 > second.x and
                            first.y < second.y + 16 and first.y + 16 > second.y)
                if overlaps:
                    first.turn()
                    second.turn()

    def mariocollision(self, previous_y=None):
        """Resolve Mario against enemies and platform tops/bottoms."""
        if previous_y is None:
            previous_y = self.mario.y
        mario_width, mario_height = 16, 24
        previous_bottom = previous_y + mario_height
        current_bottom = self.mario.y + mario_height
        self.mario.inAir = True
        self.mario.inFloor = False

        for enemy in self.enemies[:]:
            overlaps_x = (self.mario.x < enemy.x + 16 and
                          self.mario.x + mario_width > enemy.x)
            overlaps_y = (self.mario.y < enemy.y + 16 and
                          self.mario.y + mario_height > enemy.y)
            landed_on_enemy = (self.mario.yd > 0 and overlaps_x and
                               previous_bottom <= enemy.y + 2 and
                               current_bottom >= enemy.y)
            if landed_on_enemy:
                self.mario.y = enemy.y - mario_height
                self.mario.yd = -8
                self.mario.inAir = True
                if enemy.down:
                    self.enemies.remove(enemy)
                    self.addPoints(800)
                else:
                    enemy.ct = pyxel.frame_count
                    hitting(enemy, launch=False)
            elif overlaps_x and overlaps_y and not enemy.down:
                self.mario.mariohitted()

        for floor_x, floor_y in zip(self.floorX, self.floorY):
            floor_width = 16 if floor_y == 210 else 8
            overlaps_x = (self.mario.x < floor_x + floor_width and
                          self.mario.x + mario_width > floor_x)
            if not overlaps_x:
                continue

            # Land only when crossing a platform from above while descending.
            if (self.mario.yd >= 0 and previous_bottom <= floor_y + 2 and
                    current_bottom >= floor_y):
                self.mario.y = floor_y - mario_height
                self.mario.yd = 0
                self.mario.inAir = False
                self.mario.inFloor = True
            elif (self.mario.yd >= 0 and
                  abs(current_bottom - floor_y) <= 2):
                # Preserve the grounded state while standing still.
                self.mario.y = floor_y - mario_height
                self.mario.yd = 0
                self.mario.inAir = False
                self.mario.inFloor = True
            # A ceiling hit stops upward motion and triggers the POW effect.
            elif (self.mario.yd < 0 and previous_y >= floor_y + 8 and
                  self.mario.y <= floor_y + 8):
                self.mario.y = floor_y + 8
                self.mario.yd = 0
                self.enemyhit()

        # The bottom of the screen is a solid floor too.
        if self.mario.y + mario_height >= self.length - 14:
            self.mario.y = self.length - 14 - mario_height
            self.mario.yd = 0
            self.mario.inAir = False
            self.mario.inFloor = True

    def tubestp(self):
        for enemy in self.enemies:
            if enemy.x >= 306 and enemy.y in range(180, 195):
                enemy.xd = -enemy.xd
                enemy.x = 306
                enemy.y = 0
            if enemy.x <= 50 and enemy.y in range(180, 195):
                enemy.xd = -enemy.xd
                enemy.x = 50
                enemy.y = 0
        for coin in self.coins[:]:
            if coin.x == 306 and coin.y in range(190, 195):
                self.coins.remove(coin)
            if coin.x == 50 and coin.y in range(190, 195):
                self.coins.remove(coin)

    def lifeschange(self):
        if self.mario.lives == 3:
            self.lifescounter.dibujo = (0, 208, 0, 47, 16, 0)
        elif self.mario.lives == 2:
            self.lifescounter.dibujo = (0, 208, 0, 32, 16, 0)
        elif self.mario.lives == 1:
            self.lifescounter.dibujo = (0, 208, 0, 16, 16, 0)
        else:
            self.lifescounter = Lifes(140, 60)
            self.lifescounter.dibujo = (0, 176, 24, 80, 32, 0)
            self.gameOver = True

    def enemyhit(self):
        for enemy in self.enemies:
            if (self.mario.x // 1 in range(enemy.x - 16, enemy.x + 16) and
                    self.mario.y // 1 in range(enemy.y + 20, enemy.y + 24) and
                    self.mario.yd <= 0):
                enemy.ct = pyxel.frame_count
                hitting(enemy)

    def addPoints(self, points):
        self.counter.points += points
