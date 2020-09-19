class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):

        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


q = Queue()
print(q.isEmpty())
q.enqueue('naveen')
q.enqueue('oracle')
q.enqueue(1)

print(q.display())

print(q.dequeue())
print(q.display())
print(q.isEmpty())

