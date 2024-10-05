def main():
	numbers = [x for x in range(1, 6)]
	print(set([x for x in numbers if x ** 0.5 == int(x ** 0.5)]))

if __name__ == "__main__":
	main()
