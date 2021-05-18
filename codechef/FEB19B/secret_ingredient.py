# https://www.codechef.com/FEB19B/problems/CHEFING

from collections import Counter


def get_secret_ingredients(n, dishes):
    if dishes:
        c = Counter(dishes[0])
        for d in dishes[1:]:
            c &= Counter(d)

        return len(c.keys())
    else:
        return 0

def main():
    test_cases = int(input().strip())
    T = []
    for _ in range(test_cases):
        n = int(input().strip())
        dishes = []
        for _ in range(n):
            d = input().strip()
            dishes.append(d)
        T.append((n, dishes))

    # Find answer
    for (n, dishes) in T:
        print(get_secret_ingredients(n, dishes))

if __name__ == "__main__":
    main()
