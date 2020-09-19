class BalancedParanthesis(object):

    def __init__(self):
        self.stack = []
        self.brackets = {'[': ']', '{': '}', '(': ')'}

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return self.stack == []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def remove(self):
        self.stack.pop()

    def balance_check(self, s):

        for i in s:
            if i in self.brackets.keys():
                self.push(i)
            else:
                if not self.stack:
                    return False
                else:
                    top_item = self.peek()
                    if i == self.brackets[top_item]:
                        self.remove()

        return self.stack == []


bs = BalancedParanthesis()

print(bs.balance_check('[](}'))