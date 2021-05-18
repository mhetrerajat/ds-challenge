"""
Selection Sort

Sorts an array by repeatedly finding the min element from unsorted part and putting it in the beginning
"""

from bubble_sort import get_random_numbers

def sort(numbers):
    count = len(numbers)

    for i in range(count):
        min_idx = i
        for j in range(i+1, count):
            if numbers[min_idx] > numbers[j]:
               min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    
    return numbers


def main():
    numbers = get_random_numbers()
    print("Before : {0}".format(numbers))

    print("Sorted: {0}".format(sort(numbers)))

if __name__ == "__main__":
    main()
