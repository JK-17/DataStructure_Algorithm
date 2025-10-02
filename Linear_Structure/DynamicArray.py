class DynamicArray:

    """
    Initialize Dynamic Array.
    :param initial_capatiry : Starting capacity. (int, default=10)
    """
    def __init__(self, initial_capacity: int = 10):
        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be positive")

        self._array = [None] * initial_capacity
        self._capacity = initial_capacity
        self._size = 0  # current number of element


    def get(self, index: int) -> object:
        """
        Get the value at specific index
        :param index: The index of the value.
        :return: The value at specific index
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        return self._array[index]


    def set(self, index: int, value: object) -> None:
        """
        :param index: the index to set
        :param value:  The value to set
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value


    def _resize(self, new_capacity: int) -> None:
        """
        Internal method to resize the dynamic array
        :param new_capacity: new capacity (int)
        """
        new_array = [None] * new_capacity

        for i in range(self._size):
            new_array[i] = self._array[i]
            self._array = new_array
            self._capacity = new_capacity


    def append(self, value: object) -> None:
        """
        Append the value to the end of the array.
        :param value:
        """
        if self._size < self._capacity:
            self._resize(self._capacity * 2)

        self._array[self._size] = value
        self._size += 1


    def pop(self) -> object:
        """
        Remove the value from the end of the array.
        :return: The removed value
        """
        if self._size == 0:
            raise IndexError("Array is empty")

        value = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1

        # when the volume is decrease then shorten the array
        if self._size > 0 and self._size < self._capacity // 2:
            self._resize(self._capacity // 2)

        return value


    def length(self) -> int:
        """
        return the length of dynamic array
        :return: the length (int)
        """
        return self._size


