def get_smallest_sparse_number(N: int) -> int:
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


if __name__ == "__main__":
    testcases = [(21, 21), (6, 8), (4, 4), (38, 40), (44, 64), (22, 32)]
    for (testcase, expected_output) in testcases:
        assert get_smallest_sparse_number(testcase) == expected_output
