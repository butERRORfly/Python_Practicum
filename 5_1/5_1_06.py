class Rectangle:
    def __init__(self, set_1, set_2):
        self.set_1 = set_1
        self.set_2 = set_2
        self.left_down = [min(set_1[0], set_2[0]),
                          min(set_1[1], set_2[1])]
        self.up_right = [max(set_1[0], set_2[0]),
                         max(set_1[1], set_2[1])]

    def perimeter(self):
        return round((self.up_right[0] - self.left_down[0]) * 2 +
                     (self.up_right[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.up_right[0] - self.left_down[0]) *
                     (self.up_right[1] - self.left_down[1]), 2)

    def get_pos(self):
        return min(self.set_1[0], self.set_2[0]), max(self.set_1[1], self.set_2[1])

    def get_size(self):
        return round(self.up_right[0] - self.left_down[0], 2), \
            round(self.up_right[1] - self.left_down[1], 2)

    def move(self, dx, dy):
        self.set_1 = round(self.set_1[0] + dx, 2), round(self.set_1[1] + dy, 2)
        self.set_2 = round(self.set_2[0] + dx, 2), round(self.set_2[1] + dy, 2)

    def resize(self, width, height):
        self.up_right[0] = self.left_down[0] + width
        self.left_down[1] = self.up_right[1] - height
