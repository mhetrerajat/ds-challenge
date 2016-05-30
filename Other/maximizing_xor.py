#!/usr/bin/python3
# maximizing_xor.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre


def max_xor(l,r):
    return max(x^y for x in range(l,r+1) for y in range(l,r+1))

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(max_xor(l,r))
