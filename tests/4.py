list_answer = []
for _ in range(int(input())):
    num = int(input())
    list_answer.append(num)

mini = 191374839471497194713431324923843274
for i in range(1, len(list_answer)):
    if list_answer[i - 1] < list_answer[i]:
        mini = min(mini, list_answer[i])

print(mini)