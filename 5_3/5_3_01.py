def main():
    try:
        func()
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except SystemError:
        print('SystemError')
    else:
        print('No Exceptions')


if __name__ == '__main__':
    main()
