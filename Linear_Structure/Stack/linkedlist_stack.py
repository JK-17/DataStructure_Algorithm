class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._next = None

class LinkedListStack:
    def __init__(self):
        """
        Initialize your data structure here.
        top -> top node of stack
        size -> size of stack
        """
        self._top = None
        self._size = 0


    def is_empty(self) -> bool:
        """
        Check if stack is empty
        :return: bool
        """
        return self._top is None


    def size(self):
        """
        Get the size of the stack
        :return: int
        """
        return self._size


    def push(self, value: object) -> None:
        """
        Push value onto to the top of the stack
        :param value:
        :return: None
        """
        new_node = Node(value)
        new_node._next = self._top
        self._top = new_node
        self._size += 1


    def pop(self) -> object:
        """
        Removes the node from the top of the stack and returns the value
        :return: object
        """
        if self.is_empty():
            return None
        value = self._top._value
        self._top = self._top._next
        self._size -= 1
        return value


    def peek(self) -> object:
        """
        Get the node from the top of the stack
        :return: object
        """
        if self.is_empty():
            return None
        return self._top._value