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
    train = deque()
    for i in range(9):
        train.append([0,0])
    grid[(0,0)] = True
    i,j = 0,0
    for line in arg:
        # print(line, i,j)
        c = line.split()[0]
        value = int(line.split()[1])
        for _ in range(value):
            if c == "R":
                j += 1
            elif c == "L":
                j -= 1
            elif c == "D":
                i += 1
            elif c == "U":
                i -= 1
            h_now = (i,j)
            # print(i,j)
            for k,t in enumerate(train):
                # print(train)
                change = False
                offset_1 = abs(t[1]-h_now[1])
                offset_0 = abs(t[0]-h_now[0])
                if offset_1 == 2 and offset_0 == 2:
                   t[1] += 1 if h_now[1] > t[1] else -1
                   t[0] += 1 if h_now[0] > t[0] else -1
                   change = True
                elif offset_1 == 2 and offset_0 == 1:
                   t[1] += 1 if h_now[1] > t[1] else -1
                   t[0] += 1 if h_now[0] > t[0] else -1
                   change = True
                elif offset_0 == 2 and offset_1 == 1:
                   t[1] += 1 if h_now[1] > t[1] else -1
                   t[0] += 1 if h_now[0] > t[0] else -1
                   change = True
                elif offset_1 == 2:
                   t[1] += 1 if h_now[1] > t[1] else -1
                   change = True
                elif offset_0 == 2:
                   change = True
                   t[0] += 1 if h_now[0] > t[0] else -1
                if not(change):
                    break
                h_now = (t[0], t[1])
                if k == 8:
                    grid[(t[0],t[1])] = True
                # print(train)

    count = 0
    s = ""
    n = 70
    for i in range(-n,n):
        for j in range(-n,n):
            if i == 0 and j == 0:
                s += "s"
            elif grid[(i,j)]:
                s += "T"
            else:
                s += "."
        s+="\n"
    for c in grid:
        if grid[c]:
            count += 1
    # print(s)
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
