def main():
    N = int(input())
    M = int(input())
    T = int(input())
    hours = (T % (60 * 24) // 60)
    minutes = (T % 60)
    a_hours = (((hours + N) + (minutes + M) // 60) % 24)
    a_minutes = ((minutes + M) % 60)
    print(f'{a_hours:02}:{a_minutes:02}')

if __name__ == '__main__':
    main()