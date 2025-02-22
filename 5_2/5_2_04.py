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

    def __gcd(self, num1, num2):
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        return abs(num1)

    def __reduction(self):
        gcd = self.__gcd(self.__x, self.__y)
        self.__x //= gcd
        self.__y //= gcd
        return self

    def numerator(self, *args):
        match len(args):
            case 0:
                return self.__x
            case 1:
                self.__x = args[0]
                self.__reduction()
                return self.__x

    def denominator(self, *args):
        match len(args):
            case 0:
                return self.__y
            case 1:
                self.__y = args[0]
                self.__reduction()
                return self.__y

    def __str__(self):
        return f"{self.__x}/{self.__y}"

    def __repr__(self):
        return f"Fraction({self.__x}, {self.__y})"
