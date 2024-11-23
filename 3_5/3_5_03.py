from sys import stdin


def main():
    for line in stdin:
        if line[0] != '#':
            print(line.split('#')[0].rstrip('\n'))


if __name__ == '__main__':
    main()
