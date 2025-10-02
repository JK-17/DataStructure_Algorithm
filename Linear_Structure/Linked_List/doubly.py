class DNode:
    """
    node for doubly linked list
    :param value:
    """
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        """
        doubly linked list constructor
        """
        self.head = None
        self.tail = None


    def append(self, value: object) -> None:
        """
        append value to the tail of the doubly linked list
        :param value:
        """
        node = DNode(value)

        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    def prepend(self, value: object) -> None:
        """
        prepend value from the head
        :param value:
        """
        node = DNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def find(self, value: object) -> object| None:
        """
        find value in the doubly linked list
        :param value:
        :return: node or None
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None


    def remove(self, value: object) -> bool:
        """
        remove value from the tail of the doubly linked list
        :param value: specific value to remove
        """
        current = self.head
        while current and current.value != value:
            current = current.next

        if not current:
            return False

        # disconnect
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        return True

    def __iter__(self):
        """
        make list generator
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        """
        :return: print all the of the nodes
        """
        return "<->".join(str(s) for s in self)




if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.prepend(5)

    print(dll)  # 5<->10<->20

    dll.remove(10)
    print(dll)  # 5<->20

    node = dll.find(20)
    print(node.value if node else "Not found")  # 20