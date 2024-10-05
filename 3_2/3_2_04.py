def main():
	num1 = int(input())
	num2 = int(input())

	man = []
	for _ in range(num1):
		s = input()
		man.append(s)

	ovs = []
	for i in range(num2):
		s = input()
		ovs.append(s)

	counter = 0
	for i in man:
		for j in ovs:
			if i == j:
				counter += 1

	if counter == 0:
		print('Таких нет')
	else:
		print(counter)
if __name__ == '__main__':
	main()
