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
node4 = Node(4)
node5 = Node(5)

LL.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(LL)


def findElementExistsinLL(LL, value):
    node = LL.head
    while node is not None:
        if node.data == value:
            return True
        node = node.next
    return False


def deleteElement(LL, value):
    node = LL.head
    while node is not None:
        if node.next.data == value:
            node.next = node.next.next
            return LL
        node = node.next
    return "node does not exist"

def insertFront(LL, value):
    new_node = Node(value)
    new_node.next = LL.head
    LL.head = new_node
    return LL

def insertAfter(LL, value, element):
    node = LL.head
    new_node = Node(element)
    while node is not None:
        if node.data == value:
            new_node.next = node.next
            node.next = new_node
            return LL
        node = node.next
    return "Value does not exist in LL"




print(findElementExistsinLL(LL, 2))
print(deleteElement(LL, 5))
print(insertFront(LL, "wow"))
print(insertAfter(LL, "wow", "wow2"))

