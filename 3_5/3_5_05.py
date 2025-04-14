from sys import stdin


def main():
    answerWords = []
    for line in stdin:
        for word in line.split():
            if word.lower() == word[::-1].lower():
                answerWords.append(word)

    print('\n'.join(sorted(list(set(answerWords)))))


if __name__ == '__main__':
    main()
