#!/usr/bin/python3
# sherlock_and_beast.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

def decent_number(num):
    fives,threes = 0,0
    for i in range(num,-1,-1):
            if not (num-i)%5 and not i%3:
                fives = i
                threes = num-i
                break
    if fives == 0 and threes == 0:
        print(-1)
    else:
        print('5'*fives+'3'*threes)


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        decent_number(int(input()))
