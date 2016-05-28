def getInput():
    nlList = map(int, raw_input().split(" "))
    a = map(int, raw_input().split(" "))
    return nlList[0], nlList[1], a

'''
def primeFactor(n):
    if n<2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    primes = [2,3]+[i for i in range(3,n,2) if sieve[i]]
    print primes
    return sorted([primes[i] for i in range(len(primes)) if n%primes[i] == 0])[0]
'''

def prime_factors(n):
    if n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        factors=[]
        d=2
        while(d*d<=n):
            while(n>1):
                while n%d==0:
                    factors.append(d)
                    if(len(factors) == 1):
                        return factors[0]
                    n=n/d
                d+=1


def genOperationList(L):
    operationList = [(0,1,1)]
    for operation in xrange(1,L):
        print operation
        pmax = primeFactor(operation+1)
        if (pmax%(operation+1)%2) != 0:
            operationList.append((operation, 1, pmax))
        else:
            operationList.append((operation, 0, pmax))
    return operationList

def checkIfTooLarge(x):
    if x > 1000000000:
        return (x%1000000000) + 7
    else:
        return x

if __name__ == "__main__":
    try:
        #N, L, A = getInput()
        #N, L, A = 1, 500000 ,sample(range(1, 100), 1)
        N, L, A = 5,4, [2,4,5,8,10]
        if(N < 1 or L > 500000 or (len(A) != N)):
            raise Exception

        #operationList = genOperationList(L) # format -> (index, type, pmax)

        for operation in range(1,L):
            pmax = prime_factors(operation+1)
            if(len(A) != 0):
                if (pmax%(operation+1)%2 != 0):
                    maxVal = max(A)
                    maxIndex = A.index(maxVal)
                    A[maxIndex] = maxVal*2
                else:
                    minVal = min(A)
                    minIndex = A.index(minVal)
                    if(minVal/2 == 0):
                        A.remove(minVal)
                    else:
                        A[minIndex] = minVal/2
            else:
                break

        '''
        for item in operationList:
            index,type,pmax = item[0],item[1],item[2]
            if type == 1:
                maxVal = max(A)
                maxIndex = A.index(maxVal)
                A[maxIndex] = maxVal*2
            else:
                minVal = min(A)
                minIndex = A.index(minVal)
                if(minVal/2 == 0):
                    A.remove(minVal)
                else:
                    A[minIndex] = minVal/2
        '''

        print str(len(A))
        print ' '.join(map(str,map(lambda x : checkIfTooLarge(x), sorted(A))))
    except Exception,e:
        print e
