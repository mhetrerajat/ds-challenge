# https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints/0


def get_strings(n):
    return 2 * n + n * (n - 1) + n * (n - 1) / 2 + n * (n - 1) * (
        n - 2) / 2 + 1


def main():
    T = 2
    N = [1, 3]
    for n in N:
        print(int(get_strings(n)))


if __name__ == "__main__":
    main()
