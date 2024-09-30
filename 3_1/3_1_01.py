def main():
	N = int(input())
	bad = True
	for _ in range(N):
		word = input()
		if word[0] not in 'абв':
			bad = False
	if bad:
		print('YES')
	else:
		print('NO')


if __name__ == "__main__":
	main()
