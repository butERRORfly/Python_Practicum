from sys import stdin


def main():
    searchPoint = input()
    files = []
    for fileName in stdin:
        files.append(fileName.strip('\n'))

    flag = 0
    for fileName in files:
        with open(fileName, 'r') as f:
            data = ' '.join(f.read().replace(' ', ' ').lower().split())
            if searchPoint.lower() in data:
                print(fileName)
                flag = 1
    if flag == 0:
        print('404. Not Found')


if __name__ == '__main__':
    main()
