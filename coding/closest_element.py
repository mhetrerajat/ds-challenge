# Find closest element to target in sorted array



def closest(arr, target):
    if target <= arr[0]:
        return arr[0]
    elif target >= arr[-1]:
        return arr[-1]
    else:
        left = 0
        right = len(arr) - 1
        mid = 0

        while left < right:
            mid = (left+right) // 2
            
            if target < arr[mid]:
                if mid > 0 and target > arr[mid-1]:
                    if target - arr[mid-1] > arr[mid] - target:
                        return arr[mid]
                    else:
                        return arr[mid-1]

                right = mid
            else:
                if mid < len(arr) - 1 and target < arr[mid+1]:
                    if arr[mid+1] - target > target - arr[mid]:
                        return arr[mid]
                    else:
                        return arr[mid+1]

                left = mid + 1
        return arr[mid]

def main():
    N = [
        ([1, 2, 4, 5, 6, 6, 8, 9], 11, 9),
        ([2, 5, 6, 7, 8, 8, 9], 4, 5),
        ([1,2,3,4,5], 3, 3)
    ]
    for (arr, target, answer) in N:
        assert closest(arr, target) == answer


if __name__ == "__main__":
    main()
