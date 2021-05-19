# https://www.geeksforgeeks.org/print-longest-common-substring/

def get_all_substrings(s):
    substrings = []
    for i_idx, i in enumerate(s):
        _tmp = []
        for j in s[i_idx:]:
            pvs = _tmp[-1] if _tmp else None
            _tmp.append(j if not pvs else pvs + j)

        substrings.extend(_tmp)
    return substrings

def naive(s1, s2):
    s1_sub_strings = get_all_substrings(s1)
    s2_sub_strings = get_all_substrings(s2)
    
    result = None
    max_length = 0
    for x in s1_sub_strings:
        if x in s2_sub_strings and len(x) > max_length:
            max_length = len(x)
            result = x

    return result


def kmp_search(s1, s2):
    pass

def main():
    s1 = "zxabcdezy"
    s2 = "yzabcdezx"
    print(naive(s1, s2))



if __name__ == "__main__":
    main()
