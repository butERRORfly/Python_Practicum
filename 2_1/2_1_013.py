def main():
    count_of_children = int(input())
    count_of_shugar = int(input())
    print(count_of_shugar // count_of_children)
    print(count_of_shugar - count_of_children * (count_of_shugar // count_of_children))

if __name__ == '__main__':
    main()