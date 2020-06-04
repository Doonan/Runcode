#!/usr/bin/env python3
import sys
f = open(sys.argv[1], "r")
print (f.read(), end = '')
f.close()
