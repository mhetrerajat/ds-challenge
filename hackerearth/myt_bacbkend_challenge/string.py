def find_between(inputString, start, end):
    try:
        startIndex = inputString.index(start) + len(start)
        endIndex = inputString.index(end, startIndex)
        return inputString[startIndex:endIndex]
    except Exception,e:
        pass
if __name__ == "__main__":
    N = int(input())
    inputString = str(raw_input())
    if len(inputString) == N:
        qNum = int(input())
        qList = []
        for item in range(qNum):
            tempInput = str(raw_input())
            qList.append(tempInput.split(' '))

        for item in qList:
            startCh = item[0]
            endCh = item[1]
            for i in inputString:
                if i is startCh:
                    print find_between(inputString, startCh, endCh)
