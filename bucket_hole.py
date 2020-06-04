#!/usr/bin/env python3
import sys
import array
import math
arr = []
max = 0
ans = ""
if len(sys.argv) == 2:
    f = open(sys.argv[1], "r")
    for i in f:
        arr.append(int(i))
        if int(i) > max:
            max = int(i)
    #print("pre-max: " + str(max))
    max = (int(math.ceil(max / 10.0)) * 10) - 1
    #print("post-max: " + str(max))
    while max > 0:
        #print("max: " + str(max))
        count = 0
        for j in arr:
            if j in range(max-9,max+1):
                count += 1
        ans = (str(count)) + ans
        #print("max: " + str(max) + ", count: " + str(count))
        max -= 10
    print(ans)
    f.close()
