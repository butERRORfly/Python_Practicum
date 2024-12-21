class Rectangle:
    def __init__(self, set_1, set_2):
        self.set_1 = set_1
        self.set_2 = set_2

    def perimeter(self):
        return round(2 * (abs(self.set_1[0] - self.set_2[0]) + abs(self.set_1[1] - self.set_2[1])), 2)

    def area(self):
        return round((abs(self.set_1[0] - self.set_2[0]) * abs(self.set_1[1] - self.set_2[1])), 2)

    def get_pos(self):
        return self.set_1[0], self.set_2[1]

    def get_size(self):
        ...


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos())