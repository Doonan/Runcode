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
    first = float(line[0])
    second = math.floor(float(line[1])) + 1
    #print("First:",first,"  Second:",second)
    for j in range(1, second):
        if (first != 0 and j/first == math.floor(j/first)):
            print(j)
    print("")
f.close()
