def main():
	numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
	print(str(" - ".join([str(x) for x in sorted(set(numbers))])))
if __name__ == "__main__":
	main()
