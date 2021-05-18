


def get_tablet(test_cases, budget):
    max_area = -1
    for (w, h, p) in test_cases:
        if budget >= p:
            max_area = max(max_area, w*h)

    return max_area if max_area > 0 else "no tablet"

def main():
    T = int(input().strip())
    for _ in range(T):
        N, B = map(int, input().strip().split(''))
        test_cases = []
        for _ in range(N):
            widget, height, price = map(int, input().strip().split(''))
            test_cases.append((widget, height, price))

        print(get_tablet(test_cases, B))

if __name__ == "__main__":
    main()
