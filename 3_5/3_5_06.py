def main():
    dic = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'KH',
        'Ц': 'TC',
        'Ч': 'CH',
        'Ш': 'SH',
        'Щ': 'SHCH',
        'Ы': 'Y',
        'Э': 'E',
        'Ю': 'IU',
        'Я': 'IA',
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'tc',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ы': 'y',
        'э': 'e',
        'ю': 'iu',
        'я': 'ia',
    }

    with open('numbers.txt', 'r') as f:
        lines = f.readlines()

    w = ''
    for i in lines:
        for letter in i:
            if letter in dic.keys():
                if letter.istitle() is True:
                    if letter in 'ЖХЦЧШЩЮЯ':
                        w += f'{dic[letter][0]}{dic[letter][1::].lower()}'
                    else:
                        w += f'{dic[letter]}'
                else:
                    w += f'{dic[letter]}'
            elif letter not in 'ъьЪЬ':
                w += letter
            else:
                w += ''

        with open('transliteration.txt', 'w') as f:
            f.write(w)


if __name__ == '__main__':
    main()
