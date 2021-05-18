#!/usr/bin/env python

from __future__ import print_function

def limitInput(n, minN, maxN):
    if(n > maxN) or (n < minN):
        raise Exception
    else:
        return n

def getInput():
    T = limitInput(int(raw_input()), 1, 10)
    N = []
    A = []
    for i in xrange(T):
        n = limitInput(int(raw_input()), 1, 100000)
        N.append(n)
        a = map(int, raw_input().split(" "))
        A.append(a)

    return (T, N, A)

def maxContigiousSum(aItem, sum=[]):
    if not aItem:
        result, sum[:] = max(sum), [] # make sum = [] before starting new aItem
        return result
    elif len(sum) == 0:
        sum.append(aItem[0])
        return maxContigiousSum(aItem[1:], sum)
    else:
        sum.append(max(sum[len(sum)-1]+aItem[0],aItem[0]))
        return maxContigiousSum(aItem[1:], sum)

def maxNonContigiousSum(aItem, size, max_aitem, sum=0):
    if not aItem:
        result,sum = sum if sum>0 else max_aitem , 0
        return result
    elif aItem[0] > 0:
        sum += aItem[0]
        return maxNonContigiousSum(aItem[1:], size, max_aitem, sum)
    else:
        return maxNonContigiousSum(aItem[1:], size, max_aitem, sum)



if __name__ == "__main__":
    try:
        #T, N, A = getInput()
        #T, N, A = 2, [4, 6], [[1, 2, 3, 4], [2, -1, 2, 3, 4, -5]]
        T, N, A= 6, [1,6,2,3,1,6], [[1], [-1,-2,-3,-4,-5,-6], [1,-2], [1,2,3], [-10], [1,-1,-1,-1,-1,5]]
        #T, N, A = 1, [1], [[10000, -10000, 4000]]

        for aItem in A:
            print(maxContigiousSum(aItem), maxNonContigiousSum(aItem, len(aItem), max(aItem)))
    except Exception,e:
        print(e)
