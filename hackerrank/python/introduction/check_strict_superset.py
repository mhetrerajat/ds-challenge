#!/usr/bin/env python

if __name__ == "__main__":
    AList = map(int, raw_input().split(" ")); N = int(raw_input())
    NList = []
    for i in range(N):
        n = map(int, raw_input().split(" "))
        NList.append(n)

    result = True
    for i in range(N):
        result = result and (AList >= NList[i])

    print(result)
