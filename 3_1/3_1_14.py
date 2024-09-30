def main():
	numbers = list(map(int, input().split()))
	st = int(input())
	for i in numbers:
		print(f'{i ** st}', end=' ')
if __name__ == "__main__":
	main()
