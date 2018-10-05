"""
Bubble Sort
Iterate through list of numbers by comparing them in pairs and keeping smaller elements on left side by swapping them.
Do this till there is no swap in one complete iteration.
"""

import random
import copy

def sort(numbers):
    count = len(numbers)
    sorted_numbers = copy.deepcopy(numbers) # not necessary
    for _ in range(count):
        is_swap_happend = False # Keep mark whether swap happend in current iteration
        for i in range(count-1):
            a = sorted_numbers[i]
            b = sorted_numbers[i+1]
            if a > b:
                # Modify only if swap is not happend in current iteration
                if not is_swap_happend:
                    is_swap_happend = True

                # Swap
                # Keep small elements on left side
                sorted_numbers[i], sorted_numbers[i+1] = sorted_numbers[i+1], sorted_numbers[i]

        # SKip if no swap happend in last iteration
        if not is_swap_happend:
            break
    return sorted_numbers

def main():
    numbers = random.sample(range(1, 100), 10)
    sorted_numbers = sort(numbers)
    print("Before : {0} -> Sorted : {1}".format(numbers, sorted_numbers))

if __name__ == "__main__":
    main()
