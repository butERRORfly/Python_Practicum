def main():
	while stroke := input():
		if stroke[-3:] != '@@@':
			if stroke[0:2] == '##':
				stroke = stroke[2:]
			print(stroke)

if __name__ == "__main__":
	main()
