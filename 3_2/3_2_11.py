def main():
	dic = {}
	n = int(input())
	for i in range(n):
		surname = input()
		dic[surname] = dic.get(surname, 0) + 1

	counter = 0
	for i in dic.keys():
		if dic[i] != 1:
			counter += dic[i]

	print(counter)
if __name__ == '__main__':
	main()
