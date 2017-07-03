# http://practice.geeksforgeeks.org/problems/urlify-a-given-string/0


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        input_string = input().strip()
        input_length = int(input())
        print(input_string.replace(' ', '%20'))
