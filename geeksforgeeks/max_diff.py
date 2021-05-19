# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

def find_max_diff(arr):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
        min_element = min(min_element, arr[i])

    return max_diff

def main():
    arr = [1, 2, 6, 80, 100] 
    print(find_max_diff(arr))


if __name__ == "__main__":
    main()
