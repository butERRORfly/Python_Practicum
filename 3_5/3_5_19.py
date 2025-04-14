def main():
    def shift_char(c, shift):
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            return chr(start + (ord(c) - start + shift) % 26)
        return c

    def shift_string(s, shift):
        shifted = [shift_char(c, shift) for c in s]
        return ''.join(shifted)

    with open('public.txt', 'r') as f:
        text = f.readlines()

    shift = int(input())
    shifted_text = []
    for i in text:
        shifted_text.append(shift_string(i, shift))

    with open('private.txt', 'w') as f:
        f.write(''.join(shifted_text))


if __name__ == '__main__':
    main()
