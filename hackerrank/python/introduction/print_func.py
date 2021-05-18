#!/usr/bin/env python2.7
from __future__ import print_function

if __name__ == "__main__":
    N = int(raw_input())
    print(''.join(map(lambda x : str(x+1), range(N))))
