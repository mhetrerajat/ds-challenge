

def permute(arr, l, r):
    if l == r:
        print("".join(arr))
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            arr[l], arr[i] = arr[i], arr[l]

def main():
    N = ["ABC", "ABCD"]
    for n in N:
        length = len(n)
        permute(list(n), 0, length-1)
        print("="*25)


if __name__ == "__main__":
    main()
