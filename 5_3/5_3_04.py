def main():
    def only_positive_even_sum(*args):
        if all([not isinstance(x, int) for x in args]):
            raise TypeError
        elif not all():
            raise ValueError
        else:
            return sum(args)


if __name__ == '__main__':
    main()
