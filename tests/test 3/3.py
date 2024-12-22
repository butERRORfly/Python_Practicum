def count_pairs(*numbers, div=10):
    counter = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                counter += 1
    return counter