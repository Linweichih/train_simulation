class ListNode(object):
    def __init__(self, value=None, next_node=None):
        self.val = value
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_nodes(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = " -> " if node.next else "\n"
            print(node.val, end=end)
            node = node.next

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(value)


if __name__ == "__main__":
    link_list = LinkedList()
    link_list.head = ListNode(5)
    link_list.append(10)
    link_list.print_nodes()


