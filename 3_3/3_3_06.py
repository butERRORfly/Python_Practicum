def main():
	text = 'Мама мыла раму!'
	print({x.lower(): text.lower().count(x.lower()) for x in set(text.lower()) if x not in '., !?:;\n\t'})
if __name__ == "__main__":
	main()
