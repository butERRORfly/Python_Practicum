def main():
	rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
	print(str(''.join([x * y for x, y in rle])))
if __name__ == "__main__":
	main()
