class Point:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)
        self.round()

    def round(self):
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)
        return self


class Rectangle(Point):
    def __init__(self, corner1, corner2):
        self.x = min(corner1[0], corner2[0])
        self.y = max(corner1[1], corner2[1])
        self.width = round(max(corner1[0], corner2[0]) - self.x, 2)
        self.height = round(self.y - min(corner1[1], corner2[1]), 2)

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.round()

    def resize(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)

    def turn(self):
        delta = round((self.width - self.height) / 2, 2)
        self.move(delta, delta)
        self.height, self.width = self.width, self.height

    def scale(self, ratio):
        dx = round((self.width * (ratio - 1)), 2)
        dy = round((self.height * (ratio - 1)), 2)
        self.move(-dx / 2, dy / 2)
        self.resize(self.width * ratio, self.height * ratio)
