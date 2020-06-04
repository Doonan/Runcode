#!/usr/bin/env python3
import sys
import array
import math
import os

if len(sys.argv) != 2:
    sys.exit()
file = sys.argv[1]
if not os.path.isfile(file):
    sys.exit()

f = open(file, "r")
for i in f:
    line = i.split()
    first = 0
    second = 0
    if int(line[0]) < int(line[1]):
        first = int(line[0])
        second = int(line[1])
    else:
        first = int(line[1])
        second = int(line[0])
    sum = 0
    for j in range(first, second+1):
        #print(j)
        sum = sum + j
    print(sum)
f.close()
