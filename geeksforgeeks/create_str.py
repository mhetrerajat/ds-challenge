# https://practice.geeksforgeeks.org/problems/string-formation-from-substring/0/?ref=self
import sys

def find_lcs(s):
    iterations = len(s) - 1
    max_length = 0
    for i in range(iterations):
        left = s[:i+1]
        right =s[(i+1)*-1:]

        if left == right and len(left) > max_length:
            max_length = len(left)

    return max_length

def create_str(s):
    max_length = find_lcs(s)

    return False if not max_length else len(s)%(len(s)-max_length) == 0

def main():
    T = 1
    N = ["abcabcabc", "nnnvojbwijhddn"]
    for n in N:
        print(create_str(n))


if __name__ == "__main__":
    main()
