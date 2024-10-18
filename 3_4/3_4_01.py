def main():
	menu = input().split()
	print('\n'.join([str(x) + '. ' + menu[x - 1] for x in range(1, len(menu) + 1)]))


if __name__ == "__main__":
	main()
