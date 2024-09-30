def main():
	length = int(input())
	count = int(input())

	for _ in range(count):
		tabloid = input()
		if len(tabloid) <= length:
			print(tabloid)
		else:
			print(f'{tabloid[:length - 3]}...')

if __name__ == "__main__":
	main()
