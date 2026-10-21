import pyxel
#We use a new class in orther to count the points we can get
class Ui:
    def __init__(self, points: float):
        self.points = points

    def drawPoints(self):
        pyxel.text(80, 3, '{:0>9}'.format(self.points), 7)

