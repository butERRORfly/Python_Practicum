def main():
	cnt_of_start = int(input())
	breakp = 3
	bad = 0
	counter = 1
	while bad != cnt_of_start:
		for j in range(cnt_of_start):
			for i in range(breakp, 0, -1):
				print(f'До старта {i} секунд(ы)')
				if i == 1:
					print(f'Старт {counter}!!!')
					counter += 1
					breakp += 1
			break
		bad += 1
if __name__ == "__main__":
	main()
