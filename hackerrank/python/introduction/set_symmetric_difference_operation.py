#!/usr/bin/env python

if __name__ == "__main__":
    nEnglish = int(raw_input())
    englishStudents = set(map(int, raw_input().split(" ")))
    nFrench = int(raw_input())
    frenchStudents = set(map(int, raw_input().split(" ")))
    print(len(englishStudents.symmetric_difference(frenchStudents)))
