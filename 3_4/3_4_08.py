from itertools import islice, cycle


def main():
	name = [input() for _ in range(int(input()))]
	stop = int(input())
	for i in islice(cycle(name), stop):
		print(i)


if __name__ == "__main__":
	main()
