class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        element = None
        if not self.is_empty():
            element, *self.queue = self.queue
        return element

    def is_empty(self):
        return self.queue == []