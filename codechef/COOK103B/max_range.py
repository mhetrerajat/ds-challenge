import itertools


def get_max_cakes(ops, K):
    cases = itertools.combinations(ops, K)
    max_height = 0
    for item in cases:
        a,b = list(zip(*item))
        diff = abs(max(a) - min(b)) + 1 
        if diff > max_height:
            max_height = diff

    return max_height

def main():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        ops = []
        for _ in range(N):
            L, R = map(int, input().strip().split())
            ops.append((L, R))

        print(get_max_cakes(ops, K))



if __name__ == "__main__":
    main()
