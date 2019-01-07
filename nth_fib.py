# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


def fib(n):
    return dynamic(n)


def recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def dynamic(n):
    f = [0, 1]

    while len(f) < n + 1:
        f.append(0)

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


def space_efficient(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            b, a = c, b

        return c


def get_nth_fib(n):
    # 0, 1, 1, 2, 3, 5
    return fib(n)


def main():
    N = 9
    print(get_nth_fib(N))


if __name__ == "__main__":
    main()
