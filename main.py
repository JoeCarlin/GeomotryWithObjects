import turtle

from line import Line
from point import Point
from polygon import Polygon
from triangle import Triangle


def test_point(t):
    """
    Function to test the Point class
    :param t: reference to turtle used for drawing
    :return: Nothing
    """
    p1 = Point(100, 200, "red")
    p2 = Point(130, 260, "blue")
    p3 = Point(0, 0, "green")
    p1.draw(t)
    p2.draw(t)
    p3.draw(t)
    pass


def test_line(t):
    """
    Function to test the Line class
    :param t: reference to turtle used for drawing
    :return: Nothing
    """
    line1 = Line(2, 11, 200, 100, 10, "Pink")
    distance = line1.length()
    print("The distance of line1 is: ", distance)
    line1.draw(t)
    line2 = Line(-5, -7, -100, -200, 5, "Purple")
    distance = line2.length()
    print("The distance of line2 is: ", distance)
    line2.draw(t)
    pass


def test_triangle(t):
    """
    Function to test the Triangle class
    :param t: reference to turtle used for drawing
    :return: Nothing
    """
    triangle_1 = Triangle(0, 25, 200, 100, 100, 200, 5, "HotPink")
    perimeter = triangle_1.perimeter()
    print("Perimeter of triangle_1 = ", perimeter)
    triangle_1.draw(t)

    pass


def test_polygon(t):
    """
    Function to test the Polygon class
    :param t: reference to turtle used for drawing
    :return: Nothing
    """
    ## Model a polygon as a list of Points representing its vertices
    ## with the last vertex implicitly connected to the first. Thus, the number
    ## of sides for the polygon is determined by the number of points in the list

    ##This is how you will create a polygon object and interact with it
    # Uncomment the following lines for testing

    vertices = [Point(0, 100), Point(75, 150), Point(120, 120), Point(50, 50)]
    poly4 = Polygon(vertices)  # poly4 is a 4-sided polygon
    perimeter = poly4.perimeter()
    print("Perimeter of poly4 = ", perimeter)
    poly4.draw(t)

    vertices = [Point(0,-100), Point(75,-150), Point(120,-120), Point(110, -80), Point(50,-50)]
    poly5 = Polygon(vertices) #poly5 is a 5-sided polygon
    perimeter = poly5.perimeter()
    print("Perimeter of poly5 = ", perimeter)
    poly5.draw(t)

    import random
    vertices = [Point(-100,-100),Point(0,-150),Point(100,-100),Point(150,0),Point(100,100),Point(0,150),Point(-100,100),Point(-150,0)]
    num_vertices = random.randint(3,8)
    vertices = vertices[0:num_vertices]
    poly = Polygon(vertices)
    perimeter = poly.perimeter()
    print("Perimeter of poly = ", perimeter)
    poly.draw(t)
    pass


# DO NOT EDIT THE MAIN FUNCTION
# DO NOT EDIT THE MAIN FUNCTION
# DO NOT EDIT THE MAIN FUNCTION
def main():
    def pause(msg):
        """
        Pause the turtle screen till user says to continue
        :param msg: Message to show
        :return: Nothing
        """
        screen = pen.getscreen()
        screen.textinput(msg, "Press any key to continue")

    def test_all(t):
        t.clear()
        test_point(t)
        pause("Testing the Point class")

        t.clear()
        test_line(t)
        pause("Testing the Line class")

        t.clear()
        test_triangle(t)
        pause("Testing the Triangle class")

        t.clear()
        test_polygon(t)
        pause("Testing the Polygon class")

    print("Select class to test (1..5)")
    print("1. Point\n2. Line\n3. Triangle\n4. Polygon\n5. All")

    response = int(input())

    pen = turtle.Turtle()
    match response:
        case 1:
            pen.clear()
            test_point(pen)
            pause("Testing the Point class")
        case 2:
            pen.clear()
            test_line(pen)
            pause("Testing the Line class")
        case 3:
            pen.clear()
            test_triangle(pen)
            pause("Testing the Triangle class")
        case 4:
            pen.clear()
            test_polygon(pen)
            pause("Testing the Polygon class")
        case 5:
            test_all(pen)

    pen.getscreen().bye()
    pen.getscreen().mainloop()


# In PyCharm, press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
