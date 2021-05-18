# https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    words = defaultdict(int)
    for s in strings:
        words[s] += 1

    result = [0] * len(queries)
    for idx, q in enumerate(queries):
        if q in words:
            result[idx] += words[q]
        else:
            result[idx] += 0
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

