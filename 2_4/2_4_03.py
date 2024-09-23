def main():
	num = int(input())
	counter = 0
	c_pol = 1
	for i in range(1, num + 1):
		if counter != c_pol:
			print(i, end=' ')
			counter += 1
		else:
			print(f'\n{i}', end=' ')
			counter = 1
			c_pol += 1
if __name__ == "__main__":
	main()
