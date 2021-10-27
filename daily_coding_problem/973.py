"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, … z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message ‘111’ would give 3, since it could be decoded as ‘aaa’, ‘ka’, and ‘ak’.

You can assume that the messages are decodable. For example, ‘001’ is not allowed.
"""

from typing import Dict


def solution(encoded_string: str, memo: Dict[str, int]) -> int:
    length = len(encoded_string)
    if length == 1:
        return 1
    elif length == 2:
        if memo.get(encoded_string):
            nways = memo[encoded_string]
        else:
            nways = (
                is_decodable(encoded_string)
                if encoded_string.startswith("0")
                else is_decodable(encoded_string) + 1
            )
            memo[encoded_string] = nways
        return nways
    else:
        if memo.get(encoded_string[1:]):
            _nways = memo[encoded_string[1:]]
        else:
            _nways = solution(encoded_string[1:], memo)
            memo[encoded_string[1:]] = _nways
        nways_one = is_decodable(encoded_string[:1]) * _nways

        if memo.get(encoded_string[2:]):
            _nways = memo[encoded_string[2:]]
        else:
            _nways = solution(encoded_string[2:], memo)
            memo[encoded_string[2:]] = _nways
        nways_two = is_decodable(encoded_string[:2]) * _nways

        return nways_one + nways_two


def main(encoded_str: str) -> int:
    memo = {}
    nways = solution(encoded_str, memo)
    return nways


def is_decodable(enstr: str) -> int:
    if enstr.startswith("0"):
        return 0
    enstr_int = int(enstr)
    if enstr_int >= 1 and enstr_int <= 26:
        return 1
    return 0


if __name__ == "__main__":
    assert main("4123") == 3
    assert main("111") == 3
    assert main("608") == 0
    assert main("011") == 0
