def naive(N: int) -> int:
    def is_sparse(number: int) -> bool:
        prev = None
        while number != 0:
            # Remainder
            remainder = number % 2

            if prev is None:
                prev = remainder
            elif prev == remainder and remainder == 1:
                # adjacent ones
                return False
            else:
                prev = remainder

            # Quotient
            number = number // 2
        return True

    num = N
    while True:
        if is_sparse(num):
            return num
        else:
            num += 1


def get_smallest_sparse_number(N: int) -> int:
    # Build binary representation of the number
    number = N
    bins = []
    while number != 0:
        remainder = number % 2
        bins.append(remainder)
        number = number // 2

    # Add zero to the initial to avoid overflow
    bins = bins + [0]

    # bins store the binary number in reverse format
    # reverse iterate to check the trailing numbers
    prev = None
    for idx, item in enumerate(bins):
        if prev is None:
            prev = item
        elif prev == item and item == 1:
            bins[idx + 1] = 1
            for tidx in range(idx + 1):
                bins[tidx] = 0
            prev = 0
        else:
            prev = item

    result = 0
    for idx, num in enumerate(bins):
        result += 2 ** idx * num

    return result


if __name__ == "__main__":
    testcases = [(21, 21), (6, 8), (4, 4), (38, 40), (44, 64), (22, 32)]
    for (testcase, expected_output) in testcases:
        assert get_smallest_sparse_number(testcase) == expected_output
