#!/usr/bin/python3
# find_digits.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

test_cases = int(input())

for _ in range(test_cases):
    count = 0
    num = str(input())
    num_list = list(map(int,num))
    for i in num_list:
        if i!=0:
            if int(num)%i == 0:
                count+=1
    print(count)
