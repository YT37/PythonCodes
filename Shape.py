class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"The Area Is {self.side ** 2} cm"

    def perimeter(self):
        return f"The Perimeter Is {self.side*4} cm"

    def __str__(self):
        return f"This A Square Whose Area Is {self.area()} And Perimeter is {self.perimeter()}"

    def __lt__(self, other):
        return self.side < other.side

    def __eq__(self, other):
        return self.side == other.side

    def __gt__(self, other):
        return self.side > other.side


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"The Area Is {self.length * self.breadth} cm"

    def perimeter(self):
        return f"The Perimeter Is {2 * (self.length + self.breadth)} cm"

    def __str__(self):
        return f"This A Rectangle Whose Area Is {self.area()} And Perimeter is {self.perimeter()}"

    def __lt__(self, other):
        return self.length + self.breadth < other.length + other.breadth

    def __eq__(self, other):
        return self.length + self.breadth == other.length + other.breadth

    def __gt__(self, other):
        return self.length + self.breadth > other.length + other.breadth


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The Area Is {2 * (3.14 * self.radius)} cm"

    def perimeter(self):
        return f"The Perimeter Is {3.14 * (self.radius ** 2)} cm"

    def __str__(self):
        return f"This A Circle Whose Area Is {self.area()} And Perimeter is {self.perimeter()}"

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        halfp = (self.side1 + self.side2 + self.side3) / 2
        return f"The Area Is {(halfp * (halfp - self.side3) * (halfp - self.side2)* (halfp - self.side1)) ** 0.5} cm"

    def perimeter(self):
        return f"The Perimeter Is {self.side1 + self.side2 + self.side3} cm"

    def __str__(self):
        halfp = (self.side1 + self.side2 + self.side3) / 2
        return f"This A Triangle Whose Area Is {(halfp * (halfp - self.side3) * (halfp - self.side2)* (halfp - self.side1)) ** 0.5:.2f} And Perimeter is {self.perimeter()}"

    def __lt__(self, other):
        return (
            self.side1 + self.side2 + self.side3
            < other.side1 + other.side2 + other.side3
        )

    def __eq__(self, other):
        return (
            self.side1 + self.side2 + self.side3
            == other.side1 + other.side2 + other.side3
        )

    def __gt__(self, other):
        return (
            self.side1 + self.side2 + self.side3
            > other.side1 + other.side2 + other.side3
        )


class Parallelogram:
    def __init__(self, height, base, side):
        self.height = height
        self.base = base
        self.side = side

    def area(self):
        return f"The Area Is {self.height * self.base} cm"

    def perimeter(self):
        return f"The Perimeter Is {2 * (self.side + self.base)} cm"

    def __str__(self):
        return f"This A Parallelogram Whose Area Is {self.area()} And Perimeter is {self.perimeter()}"

    def __lt__(self, other):
        return (
            self.height + self.base + self.side < other.height + other.base + other.side
        )

    def __eq__(self, other):
        return (
            self.height + self.base + self.side
            == other.height + other.base + other.side
        )

    def __gt__(self, other):
        return (
            self.height + self.base + self.side > other.height + other.base + other.side
        )
