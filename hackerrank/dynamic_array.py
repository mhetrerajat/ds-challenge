#!/bin/python3

# https://www.hackerrank.com/challenges/dynamic-array/problem

import math
import os
import random
import re
import sys
import itertools

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    N = [[] for _ in range(n)]
    last_answer = 0
    result = []
    for query in queries:
        qtype, x, y = query
        if qtype == 1:
            seq_idx = (x^last_answer) % n
            N[seq_idx].append(y)
        elif qtype == 2:
            import pdb;pdb.set_trace()
            seq_idx = (x^last_answer) % n
            seq = N[seq_idx]
            idx = y % len(seq)
            last_answer = seq[idx]
            result.append(last_answer)
    
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print('\n'.join(map(str, result)))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

