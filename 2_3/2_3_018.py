def main():
    n = int(input())
    i = 2
    answer = []
    while n > 1:
        while n % i == 0:
            answer.append(i)
            n //= i
        i += 1
    answer = [str(x) for x in answer]
    print(' * '.join(answer))

if __name__ == '__main__':
    main()