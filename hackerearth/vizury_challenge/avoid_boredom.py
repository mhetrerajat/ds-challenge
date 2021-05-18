from itertools import combinations

def getInput():
    T = int(raw_input())
    nmList = map(int, raw_input().split(" "))
    A = map(int, raw_input().split(" "))
    return (T, nmList[0], nmList[1], A)

def summation(aCombinationItem):
    size = len(aCombinationItem)
    lastVal = aCombinationItem[0]
    s = 0
    for item in range(1,size):
        s += abs(lastVal-aCombinationItem[item])
        lastVal = aCombinationItem[item]
    return s

if __name__ == "__main__":
    try:
        #T, N, M, A = 1, 5, 3, [100, 50, 3000, 4000, 40]
        T,N,M,A = getInput()
        if(len(A) == N):
            aCombinations = list(combinations(A, M))

            result = []
            for acItem in aCombinations:
                s = summation(acItem)
                result.append((s, acItem))

            print(sorted(result)[-1][0])


    except Exception,e:
        print e
