def main():
	list_num = []
	for i in range(int(input())):
		number = int(input())
		list_num.append(number)
	st = int(input())
	for i in list_num:
		print(i ** st)
if __name__ == "__main__":
	main()
