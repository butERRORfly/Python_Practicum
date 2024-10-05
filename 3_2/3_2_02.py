def main():
	s1 = set(input())
	s2 = set(input())
	print(''.join(list(filter(lambda x: x in s1, s2))))
if __name__ == '__main__':
	main()
