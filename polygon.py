from point import Point


class Polygon:
    def __init__(self, vertices, thickness=5, color="HotPink"):
        self.vertices = vertices
        self.thickness = thickness
        self.color = color

    def __str__(self):
        return "Polygon with vertices: " + self.vertices

    def perimeter(self):
        perimeter = 0
        for index in range(len(self.vertices)):
            perimeter += self.vertices[index].distance(self.vertices[(index + 1) % len(self.vertices)])
        return perimeter

    def draw(self, pen):
        for index in range(len(self.vertices)):
            index = index - 1
            self.vertices[index].draw(pen)
            pen.width(self.thickness)
            pen.color(self.color)
            pen.goto(self.vertices[index + 1].x, self.vertices[index + 1].y)