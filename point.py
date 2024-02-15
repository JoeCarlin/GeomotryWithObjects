import math


class Point:
    def __init__(self, x, y, color="black"):
        self.x = x  # x properties
        self.y = y  # y properties
        self.color = color  # color properties

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def distance(self, point2):
        xdiff = (self.x - point2.x) ** 2  # self.x = P1.x
        ydiff = (self.y - point2.y) ** 2  # self.y = P1.y
        return math.sqrt(xdiff + ydiff)  # returning the sum of sqrt

    def draw(self, pen):
        pen.up()  # pick the pen up
        pen.goto(self.x, self.y)  # go to this coordinate
        pen.color(self.color)  # use self.color as the color of the dot
        pen.down()  # put pen down
        pen.dot(10)  # create a dot
