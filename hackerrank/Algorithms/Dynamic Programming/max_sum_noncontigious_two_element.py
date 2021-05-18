#!/usr/bin/env python

from __future__ import print_function

def getInput():
    T = int(raw_input())
    N = []
    A = []
    for i in xrange(T):
        n = int(raw_input())
        N.append(n)
        a = map(int, raw_input().split(" "))
        A.append(a)

    return (T, N, A)

def maxNonContigiousSumTwoElements(aItem, inclusive=[], exclusive=[]):
    if not aItem:
        result, inclusive[:], exclusive[:] = max(inclusive) if(max(inclusive) > max(exclusive[1:])) else max(exclusive[1:]),[],[]
        return result
    elif len(inclusive) == 0:
        inclusive.append(aItem[0])
        exclusive.append(0)
        print(aItem, inclusive,exclusive)
        return maxNonContigiousSum(aItem[1:], inclusive, exclusive)
    else:
        prevInclusive = inclusive[len(inclusive)-1]
        prevExclusive = exclusive[len(exclusive)-1]
        inclusive.append(max(prevInclusive, aItem[0]+prevExclusive))
        exclusive.append(prevInclusive)
        print(aItem, inclusive,exclusive)
        return maxNonContigiousSum(aItem[1:], inclusive, exclusive)
        
if __name__ == "__main__":
    try:
        #T, N, A = getInput()
        T, N, A = 2, [4, 6], [[1, 2, 3, 4], [2, -1, 2, 3, 4, -5]]
        #T, N, A= 6, [1,6,2,3,1,6], [[1], [-1,-2,-3,-4,-5,-6], [1,-2], [1,2,3], [-10], [1,-1,-1,-1,-1,5]]

        for aItem in A:
            print(maxNonContigiousSumTwoElements(aItem))
    except Exception,e:
        print(e)
