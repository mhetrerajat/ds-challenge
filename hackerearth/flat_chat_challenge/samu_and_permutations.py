def totalTaste(nItem,aItem):
    taste = 0
    for i in xrange(2,nItem):
        taste += i*(abs(aItem[i]-aItem[i-1]))
    return taste


def findTaste(aItem):
    memory=dict()
    for id, item in enumerate(aItem):
        key = (frozenset(aItem[:id] + aItem[id+1:]), item)
        memory[key] = 0

    count = 1
    best_taste = None
    while best_taste is None:
        count += 1
        anotherMemory = {}
        for (items, last), taste in memory.items():
            items = list(items)
            for id, item in enumerate(items):
                newTaste = taste + count * abs(item - last)
                newSet = frozenset(items[:id] + items[id+1:])
                if not newSet:
                    best_taste = max(newTaste, best_taste or 0)
                else:
                    newKey = newSet, item
                    anotherMemory[newKey] = max(anotherMemory.get(newKey, 0), newTaste)
        memory = anotherMemory
    return best_taste

def getInput():
    T = int(raw_input())
    N=[]
    A=[]
    for i in xrange(T):
        n = int(raw_input())
        N.append(n)
        a = map(int, raw_input().split(" "))
        A.append(a)

    return (T, N, A)

if __name__ == "__main__":
    try:
        T, N, A = getInput()

        for j in range(T):
            nItem = N[j]
            aItem = A[j]
            print findTaste(aItem)

    except Exception,e:
        print e
