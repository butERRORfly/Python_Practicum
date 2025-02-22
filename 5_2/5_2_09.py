class Fraction:
    def __init__(self, *args):
        self.__y = 1
        if isinstance(args[0], str):
            records = args[0].split('/')
            if len(records) == 1:
                self.__x = int(args[0])
            else:
                self.__x, self.__y = [int(x) for x in records]
        elif len(args) == 1 and isinstance(args[0], int):
            self.__x = int(args[0])
        else:
            self.__x = args[0]
            self.__y = args[1]
        self.__reduction()

    def __other(self, other):
        if isinstance(other, int):
            return Fraction(other, 1)
        return other

    def __pos_or_neg(self):
        return -1 if self.__x < 0 else 1

    def __lcm(self, num1, num2):
        import math
        return (num1 * num2) // math.gcd(num1, num2)

    def __gcd(self, num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return abs(num1)

    def __reduction(self):
        gcd = self.__gcd(self.__x, self.__y)
        self.__x //= gcd
        self.__y //= gcd
        if self.__y < 0:
            self.__x = -self.__x
            self.__y = abs(self.__y)
        return self

    def numerator(self, *args):
        match len(args):
            case 0:
                return abs(self.__x)
            case 1:
                self.__x = args[0] * self.__pos_or_neg()
                self.__reduction()
                return abs(self.__x)

    def denominator(self, *args):
        match len(args):
            case 0:
                return abs(self.__y)
            case 1:
                self.__y = args[0]
                self.__reduction()
                return abs(self.__y)

    def reverse(self):
        return Fraction(self.__y, self.__x)

    def __add__(self, other):
        other = self.__other(other)
        new_x = self.__x * other.__y + other.__x * self.__y
        new_y = self.__y * other.__y
        return Fraction(new_x, new_y)

    def __sub__(self, other):
        other = self.__other(other)
        new_x = self.__x * other.__y - other.__x * self.__y
        new_y = self.__y * other.__y
        return Fraction(new_x, new_y)

    def __iadd__(self, other):
        other = self.__other(other)
        self.__x = self.__x * other.__y + other.__x * self.__y
        self.__y = self.__y * other.__y
        self.__reduction()
        return self

    def __isub__(self, other):
        other = self.__other(other)
        self.__x = self.__x * other.__y - other.__x * self.__y
        self.__y = self.__y * other.__y
        self.__reduction()
        return self

    def __mul__(self, other):
        other = self.__other(other)
        new_x = self.__x * other.__x
        new_y = self.__y * other.__y
        self.__reduction()
        return Fraction(new_x, new_y)

    def __truediv__(self, other):
        other = self.__other(other)
        new = Fraction(self.__x, self.__y)
        new.__reduction()
        return new.__mul__(other.reverse())

    def __itruediv__(self, other):
        other = self.__other(other)
        return self.__imul__(other.reverse())

    def __imul__(self, other):
        other = self.__other(other)
        self.__x *= other.__x
        self.__y *= other.__y
        self.__reduction()
        return self

    def __lt__(self, other):
        other = self.__other(other)
        return self.__lcm(self.__y, other.__y) // self.__y * self.__x < self.__lcm(self.__y,
                                                                                   other.__y) // other.__y * other.__x

    def __gt__(self, other):
        other = self.__other(other)
        return self.__lcm(self.__y, other.__y) // self.__y * self.__x > self.__lcm(self.__y,
                                                                                   other.__y) // other.__y * other.__x

    def __le__(self, other):
        other = self.__other(other)
        return self.__lcm(self.__y, other.__y) // self.__y * self.__x <= self.__lcm(self.__y,
                                                                                    other.__y) // other.__y * other.__x

    def __ge__(self, other):
        other = self.__other(other)
        return self.__lcm(self.__y, other.__y) // self.__y * self.__x >= self.__lcm(self.__y,
                                                                                    other.__y) // other.__y * other.__x

    def __eq__(self, other):
        other = self.__other(other)
        return self.__lcm(self.__y, other.__y) // self.__y * self.__x == self.__lcm(self.__y,
                                                                                    other.__y) // other.__y * other.__x

    def __ne__(self, other):
        other = self.__other(other)
        return self.__lcm(self.__y, other.__y) // self.__y * self.__x != self.__lcm(self.__y,
                                                                                    other.__y) // other.__y * other.__x

    def __str__(self):
        return f"{self.__x}/{self.__y}"

    def __repr__(self):
        return f"Fraction('{self.__x}/{self.__y}')"

    def __neg__(self):
        return Fraction(-self.__x, self.__y)
