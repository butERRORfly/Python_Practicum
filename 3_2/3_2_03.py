def main():

	s = []
	for _ in range(int(input())):
		s.append(list(map(str, input().split())))

	dic = {
		'сосна': 0,
		'березка': 0,
		'волк': 0,
		'елочка': 0,
		'медведь': 0,
		'белочка': 0,
		'зайка': 0,
	}

	for i in s:
		for j in i:
			dic[j] = dic.get(j, 0) + 1

	for i in dic.keys():
		if dic[i] != 0:
			print(i)

if __name__ == '__main__':
	main()
