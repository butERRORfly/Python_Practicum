from sys import stdin


def main():
    searchPoints = []
    for line in stdin:
        searchPoints.append(line.rstrip('\n'))

    for i in searchPoints[:-1]:
        if searchPoints[-1].lower() in i.lower():
            print(i)


if __name__ == '__main__':
    main()
