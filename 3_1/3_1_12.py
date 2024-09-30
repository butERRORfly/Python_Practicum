def main():
	breakfast = {0: 'Манная', 1: 'Гречневая', 2: 'Пшённая', 3: 'Овсяная', 4: 'Рисовая'}
	stop = int(input())
	for i in range(0, stop):
		print(breakfast[i % 5])

if __name__ == "__main__":
	main()
