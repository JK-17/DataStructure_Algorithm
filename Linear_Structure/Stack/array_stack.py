class ArrayStack:
    def __init__(self):
        self._arr = []

    def is_empty(self) -> bool:
        """
        check if the stack is empty
        :return: bool
        """
        return len(self._arr) == 0

    def size(self) -> int:
        """
        get the size of the stack
        :return: size of the stack
        """
        return len(self._arr)


    def push(self, value: object) -> None:
        """
        insert element into the top of the stack
        :param value:  value to store
        """
        self._arr.append(value)


    def pop(self) -> object:
        """
        remove the element from the top of the stack
        :return: removed element
        """
        if self.is_empty():
            return None
        return self._arr.pop()


    def top(self) -> object:
        """
        get the top element of the stack
        :return: value on the top of the stack
        """
        if self.is_empty():
            return None
        return self._arr[-1]