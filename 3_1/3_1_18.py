def main():
	stroke = input()
	start = stroke[0]
	counter = 1

	for i in stroke[1::]:
		if start == i:
			counter += 1
		else:
			print(start, counter)
			start = i
			counter = 1
	print(start, counter)

if __name__ == "__main__":
	main()
