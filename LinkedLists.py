class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def display_list(self):
        current_node = self.head
        list_items = []
        while current_node:
            list_items.append(current_node.data)
            current_node = current_node.next_node
        return list_items

    def append_list(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next_node = self.head
        self.head = new_node

    def insert_after(self, target_data, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        current_node = self.head
        while current_node:
            if current_node.data != target_data:
                current_node = current_node.next_node
            elif current_node.data == target_data:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                current_node = current_node.next_node

    def insert_before(self, target_data, data):
        new_node = Node(data)

        if not target_data:
            print("List is empty")

        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data != target_data:
                prev_node = current_node
                current_node = current_node.next_node
            elif current_node.data == target_data:
                new_node.next_node = current_node
                prev_node.next_node = new_node
                current_node = current_node.next_node

    def tail_to_head(self):

        head_node = self.head
        current_node = self.head
        prev_node = None
        while current_node:
            prev_node = current_node
            current_node = current_node.next_node

        prev_node.next_node = head_node

    def cycle_check(self):

        head_node = self.head
        current_node = self.head
        while current_node:
            if current_node.next_node == head_node:
                print("this is circular linked list")
                return

            current_node = current_node.next_node

    def remove_node(self, data):

        if self.head.data == data:
            self.head = self.head.next_node

        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == data:
                prev_node.next_node = current_node.next_node
            prev_node = current_node
            current_node = current_node.next_node

    def reverse(self):

        if self.head is None:
            return self.head

        current_node = self.head
        prev_node = None
        while current_node:
            nextnode = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = nextnode
        self.head = prev_node

    def nth_to_last_node(self, n, head):
        current_node = head

        length = 0
        while current_node:
            current_node = current_node.next_node
            length += 1
        desired_node = length - n
        count = 0
        current_node = head
        while current_node:
            if count != desired_node:
                current_node = current_node.next_node
                count += 1
            else:
                print current_node.data
                return


class SumLinkedLists(object):
    sl = LinkedList()

    def __init__(self):
        pass

    def sum_list(self, list1, list2):
        p = list1.head
        q = list2.head
        carry = 0
        while p or q:

            if p:
                i = p.data
            else:
                i = 0

            if q:
                j = p.data
            else:
                j = 0

            sum_list1_2 = i + j + carry
            if sum_list1_2 >= 10:
                carry = 1
                final_num = sum_list1_2 % 10
            else:
                carry = 0
                final_num = sum_list1_2

            self.sl.append_list(final_num)
        print self.sl.display_list()
        if p.next_node:
            p = p.next_node
        if q.next_node:
            q = q.next_node

        return self.sl.display_list()


# l1.append_list(1)
# l1.append_list(2)
# l1.append_list(3)
# l1.append_list(4)
# l1.append_list(5)

a = Node(8)
b = Node(4)
c = Node(6)
d = Node(3)
e = Node(1)
l1 = LinkedList()

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
l1.nth_to_last_node(2, a)

# l1.display_list()

# l2.display_list()

#
# l.insert_at_beginning(4)
# l.insert_at_beginning(10)
# l.append_list(11)
# l.append_list(12)
# l.insert_after(4, 3)
# l.insert_before(1, 5)
# l.display_list()
# l.insert_before(5, 7)
# l.reverse()
# l.display_list()
# l.remove_node(5)
# l.tail_to_head()
# l.cycle_check()
