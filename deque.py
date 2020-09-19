class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)

    def removefront(self):
        self.items.pop()

    def removerear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


d = Deque()
