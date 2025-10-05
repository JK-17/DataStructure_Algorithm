class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        _front : front node
        _rear : rear node
        _size  : size of queue
        """
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self) -> bool:
        """
        Returns whether the queue is empty.
        :return: bool
        """
        return self._front is None

    def size(self) -> int:
        """
        Get the size of the queue.
        :return: int
        """
        return self._size

    def enqueue(self, value: object) -> None:
        """
        Adds a new item to the rear of the queue.
        :param value: data
        :return: None
        """
        if self.is_empty():
            self._front = Node(value)
            self._rear = self._front
        else:
            self._rear.next = Node(value)
            self._rear = self._rear.next

        self._size += 1

    def dequeue(self) -> object:
        """
        Removes the item from the front of the queue.
        :return: removed item from the front of the queue
        """
        if self.is_empty():
            return None

        res = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1

        return res

    def peek(self) -> object:
        """
        Get the front item of the queue.
        :return:
        """
        if self.is_empty():
            return None
        return self._front.data