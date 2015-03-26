import math

def squares_between(x, y):
    count = math.floor(math.sqrt(y)) - math.floor(math.sqrt(x - 1))
    return count


if __name__ == '__main__':
    pairs_to_check = int(input())
    for _ in range(pairs_to_check):
        x, y = tuple(int(each_pair) for each_pair in input().split())
        print(squares_between(x, y))
