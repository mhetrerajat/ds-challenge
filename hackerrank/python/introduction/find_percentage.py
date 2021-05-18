#!/usr/bin/env python2.7

def avg(dataItem):
    avg = 0.0
    for item in range(len(dataItem)):
        avg += float(dataItem[item])
    return avg/len(dataItem)

if __name__ == "__main__":
    N = int(raw_input())
    dataDict = dict()
    for i in range(N):
        dataItem = raw_input().split(" ")
        dataDict[dataItem[0]] = map(float,dataItem[1:])
    queryStudent = raw_input()

    #print(dataDict)

    #print(dataDict[queryStudent])

    print(format(avg(dataDict[queryStudent]), '.2f'))
