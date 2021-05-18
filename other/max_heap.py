import os
import timeit
from array import array


class MaxHeap(object):
    def __init__(self):
        self.heap = array("i") # signed int
    
    def _parent(self, idx):
        """
           Parent of any node is i/2 until its root.
        """
        return i/2 if i/2 > 1 else 1

    def add(self, num):
        self.heap.append(num)


    def __repr__(self):
        return ", ".join((str(v) for v in self.heap))



def main():
    max_heap = MaxHeap()
    while True:
        num = input("Enter number to add in heap: \t")
        if num in ["exit", "q"]:
            break
        else:
            num = int(num)
        max_heap.add(num)

    print(max_heap)


if __name__ == "__main__":
    main()
