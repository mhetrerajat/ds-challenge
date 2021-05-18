if __name__ == "__main__":
    T = int(input())
    N = raw_input().split(' ')
    if len(N) == T:
        for item in N:
            intItem = int(item)
            for numItem in range(intItem):
                numItem += 1
                if numItem % 3 == 0 and numItem % 5 == 0:
                    print "FizzBuzz"
                elif numItem % 5 == 0:
                    print "Buzz"
                elif numItem % 3 == 0:
                    print "Fizz"
                else:
                    print numItem
