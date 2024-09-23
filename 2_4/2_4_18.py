def main():
	num = int(input())
	c_pol = 1
	list_num = []
	counter = 0
	a = ''
	for i in range(1, num + 1):
		if counter != c_pol:
			a += f'{i} '
			counter += 1
		else:
			a += f'{i}'
			list_num.append(len(a))
			a = ''
			a += f'{i} '
			counter = 1
			c_pol += 1
	counter = 0
	width = 1
	while counter <= num:
		string = ''
		for position in range(width):
			counter += 1
			if counter <= num:
				string += str(counter)
			if position < width - 1 and counter < num:
				string += ' '
		width += 1
		print(f'{string:^{max(list_num)}}')

if __name__ == "__main__":
	main()
