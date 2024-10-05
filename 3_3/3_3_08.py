def main():
	string = 'открытое акционерное общество'
	print(''.join(([x[0][0].upper() for x in string.split()])))
if __name__ == "__main__":
	main()
