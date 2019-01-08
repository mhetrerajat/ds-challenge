# https://practice.geeksforgeeks.org/problems/longest-prefix-suffix/0


def naive(s):
    # proper prefix
    prefix = [s[:x] for x in range(len(s))]
    suffix = [s[x:] for x in range(len(s)-1, -1, -1)]

    result = [len(x) for x in prefix if x in suffix]
    return max(result) if result else 0


def better(s):
    iterations = len(s) - 1
    max_length = 0
    for i in range(iterations):
        left = s[:i+1]
        right =s[(i+1)*-1:]
        
        if left == right and len(left) > max_length:
            max_length = len(left)
            
    return max_length


def lps(s):
    return better(s)

def main():
    T = 2
    N = ["abab", "aaaa"]
    for n in N:
        print(lps(n))



if __name__ == "__main__":
    main()
