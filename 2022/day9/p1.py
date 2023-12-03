#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

import numpy as np
import re
import helper
import os
import sys

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    grid = defaultdict(lambda:False)
    i,j = 0,0
    it,jt = 0,0
    grid[(0,0)] = True
    for line in arg:
        c = line.split()[0]
        value = int(line.split()[1])
        for _ in range(value):
            ip,jp = i,j
            if c == "R":
                j += 1
            elif c == "L":
                j -= 1
            elif c == "D":
                i += 1
            elif c == "U":
                i -= 1
            if (max(abs(it-i), abs(jt-j))) == 2:
                it,jt = ip,jp
                grid[(it,jt)] = True

    count = 0
    s = ""
    n = 30
    # for i in range(-n,n):
    #     for j in range(-n,n):
    #         if grid[(i,j)]:
    #             s += "T"
    #             count += 1
    #         else:
    #             s += "."
    #     s+="\n"
    for c in grid:
        if grid[c]:
            count += 1
    print(s)
    return count

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
