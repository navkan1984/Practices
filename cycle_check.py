class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def cycle_check(self, node):

        marker1 = node
        marker2 = node

        while marker2 != None and marker2.next_node != None:

            marker1 = marker1.next_node
            marker2 = marker2.next_node.next_node
            if marker2 == marker1:
                return True

        return False

    def reverse(self, head):

        current_node = head
        prev_node = None
        next_node = None

        while current_node:

            next_node = current_node.next_node
            current_node.next_node = prev_node

            prev_node = current_node
            current_node = next_node

        return prev_node


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

a.reverse(a)
print c.next_node.value
