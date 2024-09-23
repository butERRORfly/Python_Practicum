def main():
	num = int(input())
	det = [[0] * num for _ in range(num)]
	for i in range(num):
		for j in range(num):
			det[i][j] = f'{min(i + 1, num - i, j + 1, num - j):>{len(str(num // 2 + 1))}}'
	for i in range(len(det)):
		print(*det[i])
if __name__ == "__main__":
	main()
