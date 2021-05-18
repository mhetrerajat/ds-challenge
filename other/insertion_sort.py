"""
Insertion Sort

Sorts the way we sort playing cards
"""

from bubble_sort import get_random_numbers

def sort(numbers):
    count = len(numbers)
    
    for i in range(1, count):
        is_swapped = True
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j] 
            else:
                is_swapped = False
            
            # Skip iteration if no swap has been done in last operation
            if not is_swapped:
                break
    return numbers


def main():
    numbers = get_random_numbers(length=5)
    print("Before : {0}".format(numbers))

    print("Sorted: {0}".format(sort(numbers)))

if __name__ == "__main__":
    main()
