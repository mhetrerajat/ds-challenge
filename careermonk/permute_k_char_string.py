


def permute_n_bit_k_char_strings(n, k, A):
    if n <= 0:
        print(A)
    else:
        for i in range(k):
            A[n-1] = i
            permute_n_bit_k_char_strings(n-1, k, A)

def main():
    n = 4
    k = 3
    A = [0] * n
    permute_n_bit_k_char_strings(n, k, A)



if __name__ == "__main__":
    main()
