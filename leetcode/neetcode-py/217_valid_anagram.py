# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    from collections import defaultdict

    c = defaultdict(int)
    for cs, ct in zip(s, t):
        c.setdefault(cs, 0)
        c[cs] += 1

        c.setdefault(ct, 0)
        c[ct] -= 1

    return all(v == 0 for v in c.values())


assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
assert isAnagram("hello", "world") == False  # without anagrams
assert isAnagram("abc", "abcd") == False  # different lengths
assert isAnagram("café", "éfac") == True  # anagrams with unicode chars
assert isAnagram("café", "caff") == False  # non-anagrams unicode chars
assert isAnagram("", "") == True  # empty strings
assert isAnagram("aaaabbbb", "bbbbaaaa") == True  # anagram with repeated chars
# assert isAnagram("OpenAI", "iPaEnO") == True  # mixed case
# assert isAnagram("hello, world!", "world! hello,") == True  # special chars
