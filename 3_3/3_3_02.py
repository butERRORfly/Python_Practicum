def main():
	n = int(input('n = '))
	print([[(i + 1) * (j + 1) for j in range(n)] for i in range(n)])
if __name__ == "__main__":
	main()
