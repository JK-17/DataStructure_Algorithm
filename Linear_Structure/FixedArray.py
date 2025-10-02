class FixedArray:
    """
    Initialize a fixed-size array with the given size.
    :param size: The size of the array.
    """
    def __init__(self, size: int):
        if size < 1:
            raise ValueError("size must be greater than 0")
        self._array = [None] * size
        self._size = size


    def get(self, index: int):
        """
        Get the value at specific index
        :param index: The index of the value.
        :return: The value at specific index.
        """
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._array[index]


    def set(self, index: int, value: object):
        """
        Set the value at specific index
        :param index: The index of the value.
        :param value: The value to set.
        """
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        self._array[index] = value


    def length(self) -> int:
        """
        Return the length of fixed array
        :return: The length (int)
        """
        return self._size
