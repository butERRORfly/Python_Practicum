n = int(input())
answer = []
for i in range(n):
    s = input().split(sep='%')
    answer.append(s[1][int(s[0])::-3][:int(s[-1])][::-1])

print('\n'.join(answer))