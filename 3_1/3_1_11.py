def main():
	list_stroke = []
	for i in range(int(input())):
		stroke = input()
		list_stroke.append(stroke)

	question = input()
	for i in list_stroke:
		if question.lower() in i.lower():
			print(i)

if __name__ == "__main__":
	main()
