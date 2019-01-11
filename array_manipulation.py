#!/bin/python3

# https://www.hackerrank.com/challenges/crush/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    result = [0] * (n+1)
    max_value = 0
    
    for (a,b,value) in queries:
        result[a-1] += value
        result[b] -= value

    cs = 0
    for i in result:
        cs += i
        if max_value < cs:
            max_value = cs

    return max_value



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

