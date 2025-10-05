class QueueArray:
    def __init__(self):
        """
        constructor
        """
        self._arr = []

    def is_empty(self) -> bool:
        """
        check if queue is empty
        :return: bool
        """
        return len(self._arr) == 0

    def size(self) -> int:
        """
        check the size of the queue
        :return: size of queue
        """
        return len(self._arr)

    def enqueue(self, value: object) -> None:
        """
        add element to queue
        :param value:
        :return: None
        """
        self._arr.append(value)

    def dequeue(self) -> object:
        """"
        remove element from queue
        :return: None
        """
        if self.is_empty():
            return None
        return self._arr.pop(0)

    def peek(self) -> object:
        """
        get element from queue (front element)
        :return:
        """
        if self.is_empty():
            return None
        return self._arr[0]

