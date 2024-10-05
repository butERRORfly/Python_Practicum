def main():
	dic = {}
	for _ in range(int(input())):
		enjoy = input()
		dic[enjoy] = dic.get(enjoy, 0) + 0

	for _ in range(int(input())):
		for _ in range(int(input())):
			enjoy = input()
			dic[enjoy] = dic.get(enjoy, 0) + 1

	answer = []
	for i in dic.keys():
		if dic[i] == 0:
			answer.append(i)

	if len(answer) != 0:
		print('\n'.join(sorted(answer)))
	else:
		print('Готовить нечего')


if __name__ == '__main__':
	main()
