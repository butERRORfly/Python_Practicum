def main():
	tree = input().split()
	counter = 1
	while counter <= len(tree):
		print(*tree[:counter:])
		counter += 1


if __name__ == "__main__":
	main()
