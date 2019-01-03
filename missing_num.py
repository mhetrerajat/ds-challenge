# https://www.geeksforgeeks.org/find-the-missing-number/

def get_missing_num(numbers):
    xor_all = numbers[0]
    xor_idx = 1
    for n in numbers:
        xor_all ^= n

    for idx in range(len(numbers)+2):
        xor_idx ^= idx

    return xor_all^xor_idx

def main():
    A = [1, 2, 4, 5, 6]
    n = get_missing_num(A)
    print(n)

if __name__ == "__main__":
    main()

