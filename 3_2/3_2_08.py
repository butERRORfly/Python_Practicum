def main():
	dic = {}
	for i in range(int(input())):
		enjoyer = input().split()
		for j in enjoyer[1::]:
			dic[j] = dic.get(j, []) + [enjoyer[0]]

	answer = input()
	if answer in dic:
		print('\n'.join(sorted(dic[answer])))
	else:
		print('Таких нет')

if __name__ == '__main__':
	main()
