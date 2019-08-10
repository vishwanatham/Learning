class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return Point(self.x, self.y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1 - point2)
