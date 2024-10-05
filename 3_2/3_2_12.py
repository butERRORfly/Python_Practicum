def main():
	dic = {}
	n = int(input())
	for i in range(n):
		surname = input()
		dic[surname] = dic.get(surname, 0) + 1

	a = []
	for i in dic.keys():
		if dic[i] != 1:
			a.append(f'{i} - {dic[i]}')

	if len(a) == 0:
		print('Однофамильцев нет')
	else:
		print('\n'.join(sorted(a)))

if __name__ == '__main__':
	main()
