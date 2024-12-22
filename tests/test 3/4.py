def index(text):
    for i in sorted(set({i for i in text if i.isalpha()})):
        yield i, text.find(i)