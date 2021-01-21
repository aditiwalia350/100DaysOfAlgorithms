class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


first_node = LinkedList(1)
print(first_node.data)
