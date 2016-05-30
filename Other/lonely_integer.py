#!/usr/bin/python3
# lonely_integer.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

def lonelyinteger(x):
    answer = 0
    for num in x:
        answer = answer ^ num
    return answer


if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
