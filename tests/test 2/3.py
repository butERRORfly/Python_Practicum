ints = [1, 2, 3, 4, 5]
print(sorted(ints, key=lambda digit: (int(str(digit)[-1]) <= 3)))