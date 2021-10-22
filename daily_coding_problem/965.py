def is_valid_utf8(encoded_string: str) -> bool:
    nbytes = len(encoded_string.split(" "))
    if encoded_string.startswith("0"):
        return True
    elif encoded_string.startswith("1" * nbytes + "0") and all(
        [x.startswith("10") for x in encoded_string.split(" ")[1:]]
    ):
        return True
    return False


if __name__ == "__main__":
    assert is_valid_utf8("11100010 10000010 10101100") == True
