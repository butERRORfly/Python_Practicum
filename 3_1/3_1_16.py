def main():
    breaker, counter = [int(input()) for _ in range(2)]

    text = ''
    for _ in range(counter):
        s = input()
        text += f'{s}\n'

    text.strip('\n')

    items = []
    for i in range(len(text)):
        if text[i] == '\n':
            items.append(i)

    text = text.replace('\n', '')

    if len(text) > breaker:
        text = text[:breaker - 3] + '...'

    for i in items:
        if (text[-3:] != '...') or (breaker - i >= 4):
            text = text[:i] + '\n' + text[i:]
            breaker += 1

    print(text)

if __name__ == "__main__":
    main()
