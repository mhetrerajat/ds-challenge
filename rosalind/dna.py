# http://rosalind.info/problems/dna/
import os
from collections import OrderedDict

def count(row, counter):
    for i in row:
        pv = counter.get(i, 0)
        pv += 1
        counter.update({ i : pv })
    return counter

def main():
    DATA_DIR = os.path.join(os.getcwd(), "data")
    counter = OrderedDict({ 'A': 0, 'C': 0, 'G': 0, 'T': 0})
    with open(os.path.join(DATA_DIR, "rosalind_dna.txt"), 'r') as f:
        for row in f:
            counter = count(row.strip(), counter)

    print(" ".join([str(v) for _, v in counter.items()]))

if __name__ == "__main__":
    main()
