def main():
	num = int(input())
	counter = 0
	for i in range(1, num + 1):
		for j in range(1, num + 1):
			print(f'{j} * {i} = {i * j}')
if __name__ == "__main__":
	main()
