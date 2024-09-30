def main():
	list_num = list(map(int, input().split()))

	list_num.sort()

	def q(num, deli):
		list_n = []
		for u in num:
			if u % deli == 0:
				list_n.append(u)
		if len(list_n) == len(num):
			return 1
		else:
			return -1

	list_del = []
	for j in list_num:
		for i in range(1, list_num[-1] + 1):
			if q(list_num, i) == 1:
				list_del.append(i)

	print(max(list_del))
if __name__ == "__main__":
	main()
