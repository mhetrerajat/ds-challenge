


def permute_n_bit_strings(n, A):
    if n <= 0:
        print(A)
    else:
        A[n-1] = 0
        permute_n_bit_strings(n-1, A)
        A[n-1] = 1
        permute_n_bit_strings(n-1, A)

def main():
    n = 3
    A = [0] * n
    permute_n_bit_strings(n, A)



if __name__ == "__main__":
    main()
