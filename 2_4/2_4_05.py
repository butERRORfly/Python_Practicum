def main():
	blocks = int(input())
	cnt_blocks = 0
	blocks_dic = {}
	while cnt_blocks != blocks:
		question = input()
		if 'ВСЁ' in question:
			cnt_blocks += 1
		else:
			blocks_dic[cnt_blocks] = blocks_dic.get(cnt_blocks, '') + question

	zayka_cnt = 0
	for i in blocks_dic.keys():
		if 'зайка' in blocks_dic[i]:
			zayka_cnt += 1

	print(zayka_cnt)
if __name__ == "__main__":
	main()
