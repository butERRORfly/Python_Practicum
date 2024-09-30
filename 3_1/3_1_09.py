def main():
	list_stroke = []
	while stroke := input():
		if '#' in stroke:
			index = stroke.index("#")
			if stroke[0] != '#':
				if index > 0:
					list_stroke.append(stroke[:index])
				else:
					list_stroke.append(stroke)
		else:
			list_stroke.append(stroke)
	for i in list_stroke:
		print(i)
if __name__ == "__main__":
	main()
