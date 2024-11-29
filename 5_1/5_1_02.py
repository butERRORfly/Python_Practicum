class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)
