def p1(num1, num2):
	list_del = []
	for i in range(1, max(num1, num2) + 1):
		if num1 % i == 0 and num2 % i == 0 and i:
			list_del.append(i)

	return max(list_del)


def main():
	_list = list(map(int, input().split('; ')))
	_dict = {}
	for i in _list:
		ll = [x for x in _list if x != i]
		for j in ll:
			if p1(i, j) == 1:
				_dict[i] = _dict.get(i, []) + [j]

	for i in sorted(_dict.keys()):
		print(f'{i} - {", ".join([str(x) for x in sorted(list(set(_dict[i])))])}')
if __name__ == '__main__':
	main()
