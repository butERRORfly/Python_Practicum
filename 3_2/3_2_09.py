def main():
	dic = {}
	while s := input():
		for i in s.split():
			dic[i] = dic.get(i, 0) + 1

	for i in dic:
		print(i, dic[i])

if __name__ == '__main__':
	main()
