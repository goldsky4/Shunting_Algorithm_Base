class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        return self.queue.pop(0)

    def __iter__(self):
        for i in self.queue:
            yield i