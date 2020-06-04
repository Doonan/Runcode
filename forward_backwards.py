#!/usr/bin/env python3
import sys
import array
import os

if len(sys.argv) != 2:
    sys.exit()
file = sys.argv[1]
if not os.path.isfile(file):
    sys.exit()

f = open(file, "r")
for i in f:
    it = i.rstrip('\n')
    rev = it[::-1]
    print(it == rev)
f.close()
