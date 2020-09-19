class Node:

    def __init__(self, data):
        self.data_val = data
        self.next_val = None


class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        cur_node = self.head
        elems = []
        while cur_node:
            elems.append(cur_node.data_val)
            cur_node = cur_node.next_val
        print elems

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next_val:
                curr_node = curr_node.next_val
            curr_node.next_val = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next_val = self.head
        self.head = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("\nThis node doesn't exists")
            return
        else:
            new_node = Node(data)
            new_node.next_val = prev_node.next_val
            prev_node.next_val = new_node

    def delete(self, key):

        cur_node = self.head
        prev_node = None
        if cur_node and cur_node.data_val == key:
            self.head = cur_node.next_val
            cur_node = None
            return

        while cur_node and cur_node.data_val != key:
            prev_node = cur_node
            cur_node = cur_node.next_val

        if cur_node is None:
            return
        prev_node.next_val = cur_node.next_val
        cur_node = None

    def delete_at_given_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next_val
            cur_node = None
            return

        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next_val
            count += 1

        if cur_node is None:
            return
        prev_node.next_val = cur_node.next_val
        cur_node = None


llist = LinkedList()
llist.append("Naveen")
llist.append("Manasa")
llist.append("Ria")
llist.append("Arya")
llist.display()

# llist.insert(llist.head.next_val, "Kanumuri")
# llist.delete("Ria")
llist.delete_at_given_pos(0)

llist.display()
