# counter = 0
# list_answer = []
# temporary = []
# for _ in range(int(input())):
#     while counter != 1:
#         num = input()
#         if num != 'stop':
#             temporary.append(int(num))
#         else:
#             counter += 1
#     counter = 0
#     list_answer.append(sum(temporary) / len(temporary))
#     temporary = []
# print(f'{sum(list_answer):.2f}')


def main():
    total = 0
    for _ in range(int(input())):
        tmp, counter = 0, 0
        while (num := input()) != 'stop':
            tmp += int(num)
            counter += 1
        total += tmp / counter

    print(f'{total:.2f}')


if __name__ == '__main__':
    main()