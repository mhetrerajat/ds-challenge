# https://www.geeksforgeeks.org/remove-exactly-one-element-from-the-array-such-that-max-min-is-minimum/


def get_item_to_remove(numbers):
    first_item = numbers[0]
    MAX = 99999999999999
    MIN = -9999999999999
    f_min, s_min = first_item, MAX # First and second min
    f_max, s_max = first_item, MIN # First and second max

    for i in numbers[1:]:
        if f_min >= i:
            f_min, s_min = i, f_min
        elif s_min > i:
            s_min = i

        if f_max <= i:
            f_max, s_max = i, f_max
        elif s_max < i:
            s_max = i


    f = abs(f_max - s_min)
    s = abs(s_max - f_min)

    return min(f, s)
            


def main():
    N = [2, 4, 5, 7]
    print(get_item_to_remove(N))


if __name__ == "__main__":
    main()
