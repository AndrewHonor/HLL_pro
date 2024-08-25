class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        distance = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return distance <= self.radius


circle = Circle(0, 0, 5)



point_1 = Point(3.535, 3.535)
point_2 = Point(3.536, 3.536)
print(circle.contains(point_1))
print(circle.contains(point_2))
