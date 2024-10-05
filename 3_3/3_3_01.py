def main():
	a = int(input('a = '))
	b = int(input('b = '))
	print([x ** 2 for x in range(a, b + 1)])
if __name__ == "__main__":
	main()