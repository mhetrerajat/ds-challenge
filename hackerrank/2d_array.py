#!/bin/python3

# https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_value = -(sys.maxsize)
    for i in range(4):
        for j in range(4):
            pattern_idx = sum([
               arr[i][j], arr[i][j+1], arr[i][j+2],
               arr[i+1][j+1],
               arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]
            ])
            if max_value < pattern_idx:
                max_value = pattern_idx

    return max_value


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')
    print(result)
    #fptr.close()
