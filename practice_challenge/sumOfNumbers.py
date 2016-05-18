if __name__ == "__main__":
    T = int(input())
    nList = []
    for itemT in range(T):
        N = raw_input().split(' ')
        nList.append(N)
    if len(nList) == T:
        for item in nList:
            sum = 0
            for nItem in item:
                sum += int(nItem)
            print sum
