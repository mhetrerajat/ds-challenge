#!/usr/bin/env python

from operator import add

def assignType(item):
    try:
        return int(item)
    except ValueError,e:
        return item

if __name__ == "__main__":
    nA = int(raw_input())
    AList = set(map(int, raw_input().split(" ")))
    N = int(raw_input())
    taskList = []
    taskValList = []
    for i in range(2*N):
        if(i%2 == 0):
            taskList.append(map(assignType, raw_input().split(" ")))
        else:
            taskValList.append(map(int, raw_input().split(" ")))

    for i in range(N):
        if taskList[i][0] == "intersection_update":
            AList.intersection_update(taskValList[i])
        elif taskList[i][0] == "update":
            AList.update(taskValList[i])
        elif taskList[i][0] == "symmetric_difference_update":
            AList.symmetric_difference_update(taskValList[i])
        elif taskList[i][0] == "difference_update":
            AList.difference_update(taskValList[i])

    if(len(AList)):
        print(reduce(add, list(AList)))
    else:
        print(0)
