class Rectangle:
    def __init__(self, set_1, set_2):
        self.set_1 = set_1
        self.set_2 = set_2

    def perimeter(self):
        return round(2 * (abs(self.set_1[0] - self.set_2[0]) + abs(self.set_1[1] - self.set_2[1])), 2)

    def area(self):
        return round((abs(self.set_1[0] - self.set_2[0]) * abs(self.set_1[1] - self.set_2[1])), 2)

    def get_pos(self):
        return min(self.set_1[0], self.set_2[0]), max(self.set_1[1], self.set_2[1])

    def get_size(self):
        return round(abs(abs(self.set_1[0]) - abs(self.set_2[0])), 2), round(
            abs(abs(self.set_1[1]) - abs(self.set_2[1])), 2)

    def move(self, dx, dy):
        self.set_1 = round(self.set_1[0] + dx, 2), round(self.set_1[1] + dy, 2)
        self.set_2 = round(self.set_2[0] + dx, 2), round(self.set_2[1] + dy, 2)


    def resize(self, width, height):
        ...

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())