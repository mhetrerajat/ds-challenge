def getInput():
    N = int(raw_input())
    hlList = []
    for i in xrange(N):
        hl = map(int, raw_input().split(" "))
        hlList.append(hl)
    return (N, hlList)

def getMaxHappiness(hlList):
    buyedItems = []
    maxHappiness = 0
    for item in hlList:
        h,l = item[0], item[1]
        if len(buyedItems) == 0:
            maxHappiness += h
            buyedItems.append(item)
        elif buyedItems[-1][1] <= l:
            maxHappiness += h
            buyedItems.append(item)
    return maxHappiness

def checkHL(hlItem):
    result = True
    for hlItem in hlList:
        if((abs(hlItem[0]) >= 1) and (abs(hlItem[0]) <= 100000)) and ((hlItem[1] >= 1) and (hlItem[1] <= 1000000000000000000)):
            result = result and True
        else:
            result = result and False
            break
    return result

if __name__ == "__main__":
    try:
        N, hlList = 5, [[10, 2], [-10, 1], [5, 2], [5, 2], [10, 3]]
        #N, hlList = 1, [[100000, 1000000000000000000000000000000]]
        #N, hlList = getInput()
        token = checkHL(hlList)
        if ((1 > N) or (N > 100000)) and (len(hlList) != N) and not token:
            raise Exception
        maxHappiness = getMaxHappiness(hlList)
        print maxHappiness
    except Exception,e:
        print e
