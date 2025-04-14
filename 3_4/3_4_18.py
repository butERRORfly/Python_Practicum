from itertools import permutations, combinations, product


def main():
	f = input()
	print('a b c f')
	for a, b, c in product([0, 1], repeat=3):
		print(a, b, c, int(eval(f, {'a': a, 'b': b, 'c': c})))


if __name__ == "__main__":
	main()
