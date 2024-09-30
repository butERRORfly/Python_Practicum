def main():
	stroke = list(map(str, input().split()))

	answer = []
	while len(stroke) != 0:
		a = stroke.pop(0)
		if a not in '-+*':
			answer.append(int(a))
		else:
			if a == '-':
				answer.append(answer.pop(-2) - answer.pop())
			if a == '+':
				answer.append(answer.pop(-2) + answer.pop())
			if a == '*':
				answer.append(answer.pop(-2) * answer.pop())

	print(*answer)



if __name__ == "__main__":
	main()
