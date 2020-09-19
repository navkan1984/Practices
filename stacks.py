class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()

s.push('naveen')
print(s.peek())

s.push('1984')

s.push('Arya')

print(s.isEmpty())

print(s.pop())
s.pop()
s.pop()
print(s.isEmpty())