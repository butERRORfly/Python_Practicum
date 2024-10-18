def main():
	mum, dad, daughter = [input().split(', ') for _ in range(3)]
	_set = sorted({*mum, *dad, *daughter})
	print("\n".join([str(x) + '. ' + _set[x - 1] for x in range(1, len(_set) + 1)]))


if __name__ == "__main__":
	main()
