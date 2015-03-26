#!/usr/bin/python3
# service_lane.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

n,t = map(int, input().split())

width = list(map(int, input().split()))

for _ in range(t):
    i,j = map(int, input().split())
    vehicle = min(width[segment] for segment in range(i,j+1))
    print(vehicle)
