def main():
	_dic = {}
	for i in range(int(input())):
		x, y = list(map(int, input().split()))
		_dic[(int(x) // 10, int(y) // 10)] = _dic.get((int(x) // 10, int(y) // 10), 0) + 1

	print(max(x[1] for x in _dic.items()))

if __name__ == '__main__':
	main()
