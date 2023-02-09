"""""" """
This problem was asked by Twitter.

You are given an array of length 24, where each element represents 
the number of new subscribers during the corresponding hour. 
Implement a data structure that efficiently supports the following:

    update(hour: int, value: int): Increment the element at index hour by value.
    query(start: int, end: int): Retrieve the number of subscribers that have signed 
                            up between start and end (inclusive).

You can assume that all values get cleared at the end of the day, 
and that you will not be asked for start and end values that wrap around midnight.
""" """"""


class Subscribers:
    def __init__(self) -> None:
        self._data = [0] * 24

    def update(self, hour: int, value: int) -> None:
        self._data[hour] += value

    def query(self, start: int, end: int) -> int:
        total = 0
        for idx in range(start, end + 1):
            total += self._data[idx]
        return total


if __name__ == "__main__":
    subs = Subscribers()
    subs.update(4, 5)
    subs.update(2, 9)
    assert subs.query(2, 5) == 14
