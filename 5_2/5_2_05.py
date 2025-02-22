class Fraction:
    def __init__(self, *args):
        match isinstance(args[0], str):
            case 1:
                self.__x = int(args[0].split('/')[0])
                self.__y = int(args[0].split('/')[1])
            case 0:
                self.__x = int(args[0])
                self.__y = int(args[1])
        self.__reduction()

    def __pos_or_neg(self):
        return -1 if self.__x < 0 else 1

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

    def __str__(self):
        return f"{self.__x}/{self.__y}"

    def __repr__(self):
        return f"Fraction('{self.__x}/{self.__y}')"

    def __neg__(self):
        return Fraction(-self.__x, self.__y)
