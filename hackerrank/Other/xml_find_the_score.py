#!/usr/bin/python3
# xml_find_the_score.py
# Author : Rajat Mhetre
# follow and drop me a line at @rajat_mhetre

import xml.etree.ElementTree as etree

count = 0

lines = int(input())
xml = ""
for _ in range(lines):
    xml += str(input())

tree = etree.ElementTree(etree.fromstring(xml))

for element in tree.iter():
    count += len(element.attrib)

print(count)
