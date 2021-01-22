class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


LL = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

LL.head = node1
node1.next = node2
node2.next = node3

print(LL)


def findElementExistsinLL(LL, value):
    node = LL.head
    while node is not None:
        if node.data == value:
            return True
        node = node.next
    return False


print(findElementExistsinLL(LL, 2))
