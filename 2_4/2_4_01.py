def main():
	num = int(input())
	for i in range(num):
		for j in range(num):
			print((i + 1) * (j + 1), end=' ')
		print()

if __name__ == "__main__":
	main()
