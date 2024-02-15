from point import Point


class Line:

    def __init__(self, start_x, start_y, end_x, end_y, thickness=2, color="Black"):
        self.start = Point(start_x, start_y)  # properties
        self.end = Point(end_x, end_y)  # properties
        self.thickness = thickness  # properties
        self.color = color  # properties

    def __str__(self):
        return str(self.start) + " to " + str(self.end)

    def length(self):
        return self.start.distance(self.end)

    def slope(self):
        ydiff = self.end.y - self.start.y
        xdiff = self.end.x - self.start.x
        return ydiff / xdiff

    def draw(self, pen):
        # draw the start point
        self.start.draw(pen)
        pen.down()
        pen.width(self.thickness)
        pen.color(self.color)
        pen.goto(self.end.x, self.end.y)
        self.end.draw(pen)
