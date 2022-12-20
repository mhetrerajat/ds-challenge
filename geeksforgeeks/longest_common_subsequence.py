


# Length of longest common subsequence

def _lcs(a, b, la, lb):
    if la == 0 or lb == 0:
        return 0
    elif a[la-1] == b[lb-1]:
        return 1 + _lcs(a,b,la-1, lb-1)
    else:
        # a[la-1] != b[lb-1]
        return max(_lcs(a,b, la-1, lb), _lcs(a,b, la, lb-1)) 

def _lcs_memo(a, b, la, lb, memo):
    if 

def lcs(a, b):
    length_a = len(a)
    length_b = len(b)

    return _lcs(a, b, length_a, length_b)

if __name__ == "__main__":
    assert(lcs("ABCDGH", "AEDFHR")) == 3
    assert(lcs("AGGTAB", "GXTXAYB")) == 4
