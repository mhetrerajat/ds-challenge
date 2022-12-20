# https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0

import math

def getMinTime(paintersAllowed, size, boards):
    minTime, maxTime = max(boards), sum(boards)
    return binSearch(minTime, maxTime, boards, paintersAllowed)


def binSearch(minTime, maxTime, boards, paintersAllowed):
    solution = 0
    while minTime <= maxTime:
        mid = math.floor((maxTime + minTime) / 2)
        print('minTime', minTime, 'mid', mid, 'maxTime', maxTime)

        paintersNeeded = findPaintersNeeded(boards, mid)
        print('paintersNeeded', paintersNeeded, 'solution', solution)

        if paintersNeeded > paintersAllowed:
            minTime = mid + 1
        else:
            maxTime = mid - 1
            solution = mid
        '''
        print('paintersNeeded', paintersNeeded, 'solution', solution)
        print()'''
    return solution


def findPaintersNeeded(boards, timeCheck):
    sum = 0
    paintersNeeded = 1

    for length in boards:
        sum = sum + length

        if sum > timeCheck:
            paintersNeeded = paintersNeeded + 1
            sum = length

    return paintersNeeded


def main():
    T = 2
    for (n, k, A) in [(2, 4, [10, 10, 10, 10]), (2, 4, [10, 20, 30, 40])]:
        minTime = getMinTime(n, k, A)
        print(minTime)


if __name__ == "__main__":
    main()
