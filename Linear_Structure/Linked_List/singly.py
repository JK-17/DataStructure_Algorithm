class Node:

    def __init__(self, value: object):
        """
        node for singly linked list
        :param value:
        """
        self.value = value
        self.next = None

class SinglyLinkedList:


    def __init__(self):
        """
        construct head and tail of linked list
        """
        self.head = None
        self.tail = None


    def append(self, value: object):
        """
        append value from the tail
        :param value: The value
        """
        node = Node(value)

        # if head is empty
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def prepend(self, value: object):
        """
        prepend value from the head
        :param value:
        """
        node = Node(value)
        node.next = self.head
        self.head = node

        # if tail is empty
        if not self.tail:
            self.tail = node


    def find(self, value: object) -> object:
        """
        find value from the head
        :param value: Searching Value
        :return: searching value or None
        """
        current = self.head

        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, value: object) -> bool:
        previous, current = None, self.head

        # loop O(n) find the value(node) and previous node
        while current and current.value != value:
            previous = current
            current = current.next

        # no node found from the loop -> false (Fail to delete)
        if not current:
            return False

        # if there is previous node
        # disconnect the current node (the deleting one)
        if previous:
            previous.next = current.next
        else:
            # if there is no previous
            # assume current is head
            self.head = current.next

        # if current is tail
        # make previous tail
        if current == self.tail:
            self.tail = previous

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
        return "->".join(str(s) for s in self)