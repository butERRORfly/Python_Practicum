def main():
    left = 1
    right = 1000
    counter = 0
    while counter != 10:
        current = (left + right) // 2
        print(current)
        is_right = input()
        if is_right == 'Угадал!':
            break
        elif is_right == 'Больше':
            left = current + 1
        else:
            right = current - 1
        counter += 1


if __name__ == '__main__':
    main()