def main():
	counter = 0
	for _ in range(int(input())):
		word = input()
		counter += word.count('зайка')
	print(counter)
if __name__ == "__main__":
	main()
