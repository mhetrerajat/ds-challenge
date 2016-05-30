# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

t = int(input())

for _ in range(t):
    cycle_count = int(input())
    height = 1

    for i in range(cycle_count):
        if(i%2 == 0):
            height *= 2
        else:
            height += 1

    print(height)
