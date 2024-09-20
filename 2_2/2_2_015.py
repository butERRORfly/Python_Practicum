def main():
    num1 = int(input())
    num2 = int(input())

    num_glob = str(num1) + str(num2)
    num_glob_list = sorted([int(x) for x in num_glob], reverse=True)
    print(f'{num_glob_list[0]}{sum(num_glob_list[1:3]) % 10}{num_glob_list[-1]}')

if __name__ == '__main__':
    main()