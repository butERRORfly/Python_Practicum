def main():
	num = int(input())
	list_zayka = []
	for _ in range(num):
		stroke = input()
		if 'зайка' in stroke:
			mini = 9383247198471934
			for i in range(1, len(stroke) + 1):
				if stroke[i - 1] == 'з' and stroke[i] == 'а':
					mini = min(mini, i)
			list_zayka.append(str(mini))
		else:
			list_zayka.append('Заек нет =(')
	for i in list_zayka:
		print(i)
if __name__ == "__main__":
	main()
