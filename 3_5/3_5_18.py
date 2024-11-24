import os
import math


def main():
    file = input()

    def getSizeFile(file):
        sizeBytes = os.path.getsize(file)
        return sizeBytes

    sizes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    index = 0

    data = getSizeFile(file)
    while data >= 1024 and index < len(sizes) - 1:
        index += 1
        data /= 1024

    print(f'{math.ceil(data)}{sizes[index]}')


if __name__ == '__main__':
    main()
