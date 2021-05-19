# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/0

T = 2
S = [(9, 5, [1, 3, 5, 5, 5, 5, 67, 123, 125]),
     (9, 7, [1, 3, 5, 5, 5, 5, 7, 123, 125])]


def bsearch(x, _max, _min, idx):
    mid = (_min + _max) // 2

    if x > mid:
        # Go right
        return bsearch(x, _max, mid)
    elif x < mid:
        # Go left
        return bsearch(x, mid, _min)
    else:
        return True


def find_occurrence(n, x, a):
    _min, _max = a[0], a[-1]
    idx = -1
    return bsearch(x, _max, _min)


for (n, x, a) in S:
    print(find_occurrence(n, x, a))
