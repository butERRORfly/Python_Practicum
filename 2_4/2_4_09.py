def main():
	answer = ''
	for i in range(int(input())):
		num = int(input())
		answer += str(max([int(x) for x in str(num)]))
	print(answer)

if __name__ == "__main__":
	main()
