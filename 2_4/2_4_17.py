def main():
	list_num = [int(input()) for _ in range(int(input()))]
	counter = 0
	for i in list_num:
		if str(i) == str(i)[::-1]:
			counter += 1
	print(counter)
if __name__ == "__main__":
	main()
