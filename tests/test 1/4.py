# list_answer = []
# for _ in range(int(input())):
#     num = int(input())
#     list_answer.append(num)
#
# mini = 191374839471497194713431324923843274
# for i in range(1, len(list_answer)):
#     if list_answer[i - 1] < list_answer[i]:
#         mini = min(mini, list_answer[i])
#
# print(mini)


def main():
    mini = int(1e12)
    tmp = int(1e12)
    for _ in range(int(input())):
        num = int(input())
        if tmp < num:
            mini = min(mini, num)
        tmp = num

    print(mini)


if __name__ == '__main__':
    main()