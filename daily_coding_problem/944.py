def next_permutation(number: int) -> int:

    number_as_str = str(number)

    prev = 0
    swap_point_idx = -1
    for idx, num in enumerate(number_as_str[::-1]):
        num_idx = abs(idx - len(number_as_str)) - 1
        if prev > int(num):
            swap_point_idx = num_idx
            break
        else:
            prev = int(num)

    # Not possible to find next largest number
    if swap_point_idx == -1:
        return -1

    # Find next largest number after swap point
    next_largest_idx = -1
    swap_point_num = int(number_as_str[swap_point_idx])
    prev_largest_num = swap_point_num
    for idx, num in enumerate(number_as_str[swap_point_idx + 1 :]):
        num = int(num)
        if num > swap_point_num and (
            prev_largest_num > num or prev_largest_num == swap_point_num
        ):
            prev_largest_num = num
            next_largest_idx = idx + swap_point_idx + 1

    # Swap numbers now
    number_as_str = list(number_as_str)
    number_as_str[swap_point_idx], number_as_str[next_largest_idx] = (
        number_as_str[next_largest_idx],
        number_as_str[swap_point_idx],
    )

    # Reverse the subsequent numbers in ascending order
    number_as_str[swap_point_idx + 1 :] = list(
        reversed(number_as_str[swap_point_idx + 1 :])
    )

    return int("".join(number_as_str))


if __name__ == "__main__":
    assert next_permutation(48975) == 49578
    assert next_permutation(218765) == 251678
    assert next_permutation(1234) == 1243
    assert next_permutation(4321) == -1
    assert next_permutation(534976) == 536479
