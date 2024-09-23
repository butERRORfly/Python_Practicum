def main():
	list_summa = []
	for i in range(int(input())):
		num = int(input())
		list_summa.append(num)

	summa = 0
	for i in list_summa:
		summa += sum(int(x) for x in str(i))

	print(summa)
if __name__ == "__main__":
	main()
