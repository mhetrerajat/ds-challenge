#!/usr/bin/python3
# max_min.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

n = int(input())
k = int(input())
num_list = [int(input()) for _ in range(0,n)]
num_list.sort()
min_unfairness = 1000000000

for i in range(n - k + 1):
    min_unfairness = min(min_unfairness, num_list[i+k-1] - num_list[i])

print(min_unfairness)
