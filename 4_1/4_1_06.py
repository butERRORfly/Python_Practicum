previous = set()


def modern_print(string):
    if string not in previous:
        print(string)
    previous.add(string)
