#!/usr/bin/python3
# isFibo.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

def square_check(n):
    n = n**0.5
    return int(n)==n

def check_fibo(n):
    if(square_check((5*n*n+4)) or square_check((5*n*n-4))):
        return print("IsFibo")
    else:
        return print("IsNotFibo")

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        num = int(input())
        check_fibo(num)
