def main():
	bad = 0
	text = ''
	while bad != -1:
		stroke = input()
		if stroke != 'ФИНИШ':
			text += stroke
		else:
			bad = -1

	dic_text = {}
	for i in text.lower():
		if i != ' ':
			dic_text[i] = dic_text.get(i, 0) + text.lower().count(i)

	sorted_dic = sorted(dic_text.items(), key=lambda item: item[0])
	sorted_dic = sorted(dic_text.items(), key=lambda item: item[1], reverse=True)
	print(sorted_dic[0][0])

if __name__ == "__main__":
	main()
