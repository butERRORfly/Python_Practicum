def main():
    with open('secret.txt', 'r') as f:
        data = f.readlines()

    def binStep(num):
        if num > 128:
            return chr(num % 256)
        else:
            return chr(num)

    result = ''
    for line in data:
        for char in line:
            result += binStep(ord(char))

    print(result)


if __name__ == '__main__':
    main()
