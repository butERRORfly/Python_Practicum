from itertools import combinations as porno


def main():
	name = [input() for _ in range(int(input()))]
	for i in list(porno(name, 2)):
		print(f'{i[0]} - {i[1]}')


if __name__ == "__main__":
	main()
