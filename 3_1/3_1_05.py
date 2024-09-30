def main():
	word = input()
	if word == word[::-1]:
		print('YES')
	else:
		print('NO')
if __name__ == "__main__":
	main()
