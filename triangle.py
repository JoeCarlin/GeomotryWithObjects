from point import Point


class Triangle:
    def __init__(self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, thickness=2, color="Black"):
        self.p1 = Point(p1_x, p1_y)  # properties
        self.p2 = Point(p2_x, p2_y)  # properties
        self.p3 = Point(p3_x, p3_y)  # properties
        self.thickness = thickness  # properties
        self.color = color  # properties

    def __str__(self):
        return "Triangle Points: " + str(self.p1) + "," + str(self.p2) + "," + str(self.p3)

    def perimeter(self):
        perimeter = self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)
        return perimeter

    def draw(self, pen):
        # draw the start point
        self.p1.draw(pen)
        pen.down()
        pen.width(self.thickness)
        pen.color(self.color)
        pen.goto(self.p2.x, self.p2.y)
        self.p2.draw(pen)
        pen.down()
        pen.width(self.thickness)
        pen.color(self.color)
        pen.goto(self.p3.x, self.p3.y)
        self.p3.draw(pen)
        pen.down()
        pen.width(self.thickness)
        pen.color(self.color)
        pen.goto(self.p1.x, self.p1.y)