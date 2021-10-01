def get_nth_perfect_num(N: int) -> int:
    def is_perfect(num: int) -> bool:
        sum = 0
        while num > 0:
            remainder = num % 10
            num = num // 10
            sum += remainder

        return sum == 10

    num = 18
    nth_num = N
    while True:
        if is_perfect(num):
            nth_num -= 1
            if nth_num == 0:
                return num
        num += 1


if __name__ == "__main__":
    assert get_nth_perfect_num(1) == 19
    assert get_nth_perfect_num(11) == 118
    assert get_nth_perfect_num(10) == 109
