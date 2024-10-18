def main():
	num = int(input())
	print('А Б В')
	for i in range(1, num + 1):
		for j in range(1, num + 1):
			for k in range(1, num + 1):
				if i + j + k == num:
					print(f'{i} {j} {k}')


if __name__ == "__main__":
	main()
