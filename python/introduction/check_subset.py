#!/usr/bin/env python

if __name__ == "__main__":
    T = int(raw_input())
    AList = []
    BList = []
    for i in range(T):
        a = int(raw_input())
        aList = map(int, raw_input().split(" "))
        AList.append((a, aList))
        b = int(raw_input())
        bList = map(int, raw_input().split(" "))
        BList.append((b, bList))

    for i in range(T):
        a = AList[i][1]
        b = BList[i][1]
        if(set(a) < set(b)):
            print("True")
        else:
            print("False")

    '''
    for i in range(int(raw_input())):
        a = int(raw_input()); A = set(map(int,raw_input().split(" ")))
        b = int(raw_input()); B = set(map(int,raw_input().split(" ")))
        print(A < B)
    '''
