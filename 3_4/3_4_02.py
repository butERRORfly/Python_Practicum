def main():
	names1, names2 = [input().split(', ') for _ in range(2)]
	if len(names1) < len(names2):
		names2.pop(-1)
	elif len(names1) > len(names2):
		names1.pop(-1)
	print('\n'.join([names1[x] + ' - ' + names2[y] for x in range(len(names1)) for y in range(len(names2)) if x == y]))


if __name__ == "__main__":
	main()
