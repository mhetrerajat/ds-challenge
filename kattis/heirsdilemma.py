# https://open.kattis.com/problems/heirsdilemma

def check_divisibility(n):
    tmp = n
    already_marked_digits = [0] * 10
    while tmp > 0:
        digit = tmp % 10

        if digit == 0:
           return False

        if already_marked_digits[digit] > 0:
           return False

        if n % digit != 0:
            return False
        
        already_marked_digits[digit] += 1
        tmp = tmp // 10

    return True

def check(l,h):
    count = 0
    for i in range(l,h+1,1):
        if check_divisibility(i):
            count += 1
    
    return count

def main():
    t = input().split(" ")
    l, h = [int(x.strip()) for x in t]
    print(check(l,h))


if __name__ == "__main__":
    main()
