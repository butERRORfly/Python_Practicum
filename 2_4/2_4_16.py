def main():
	height, width = [int(input()) for _ in range(1, 3)]
	for i in range(height):
		for j in range(height):
			print(f'{(i + 1) * (j + 1):^{width}}', end='')
			if j + 1 != height:
				print('|', end='')
			else:
				print()
		if i + 1 != height:
			print('-' * (height * width + height - 1))


if __name__ == "__main__":
	main()