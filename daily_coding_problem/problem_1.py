"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def main():
    nums = [10, 15, 3, 7]
    target = 17
    
    d = {}
    for i in nums:
        key = target - i 
        if d.get(i) is not None:
            print([i, key])

        d[key] = i

if __name__ == "__main__":
    main()
