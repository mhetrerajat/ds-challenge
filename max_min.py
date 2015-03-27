#!/usr/bin/python3
# max_min.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

n = int(input())
k = int(input())
num_list,k_list = [],[]

for _ in range(n):
    num = int(input())
    num_list.append(num)

num_list.sort()
k_list = num_list[:k]
print(max(k_list)-min(k_list))
