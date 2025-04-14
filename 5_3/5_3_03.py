def main():
    class Error:
        def __repr__(self):
            raise Exception

    ya = Error()
    func(ya)


if __name__ == '__main__':
    main()
