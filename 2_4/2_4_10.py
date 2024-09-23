def main():
	count = int(input())
	print('А Б В')
	for i in range(1, count + 1):
		for j in range(1, count + 1):
			for k in range(1, count + 1):
				if i + j + k == count:
					print(i, j, k)

if __name__ == "__main__":
	main()
