import timeit
from array import array
import os

def max_heapify(heap, num):
    print(heap, num)
    return heap

def main():
    heap = array('I')
    while True:
        num = input("Enter number to add in heap: \t")
        if num in ["exit", "q"]:
            break
        else:
            num = int(num)
        heap = max_heapify(heap, num)



if __name__ == "__main__":
    main()
