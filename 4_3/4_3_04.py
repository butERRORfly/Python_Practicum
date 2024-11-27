def answer(oldFunc):
    def newFunc(*args, **kwargs):
        return f'Результат функции: {oldFunc(*args, **kwargs)}'
    return newFunc