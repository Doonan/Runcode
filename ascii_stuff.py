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

ans = ''
f = open(file, "r")
line = f.readline()
hexes = line.split()
for i in hexes:
    ans = ans + bytes.fromhex(i).decode('utf-8')
print(ans)
f.close()
