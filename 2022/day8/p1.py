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
    # argnum = list(map(int, arg))
    grid = defaultdict(lambda:False)
    nb = 0
    n = len(arg)
    for i in range(n):
        for j in range(n):
            if j == 0 or i == 0 or j == n-1 or i == n-1:
                grid[(i,j)] = True

    for i in range(n):
        skip_side_1 = int(arg[i][0])
        skip_side_2 = int(arg[0][i])
        skip_side_3 = int(arg[i][n-1])
        skip_side_4 = int(arg[n-1][i])
        for j in range(1,n-1):
            if int(arg[i][j]) > skip_side_1:
                grid[(i,j)] = True
                skip_side_1 = int(arg[i][j])
            if int(arg[j][i]) > skip_side_2:
                skip_side_2 = int(arg[j][i])
                grid[(j,i)] = True
            jp = n - j - 1
            if int(arg[i][jp]) > skip_side_3:
                grid[(i,jp)] = True
                skip_side_3 = int(arg[i][jp])
            if int(arg[jp][i]) > skip_side_4:
                grid[(jp,i)] = True
                skip_side_4 = int(arg[jp][i])
    count = 0
    s = ""
    for i in range(n):
        for j in range(n):
            if grid[(i,j)]:
                s += "1"
                count += 1
            else:
                s += "0"
        s+="\n"
    print(s)
    # print(grid)
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
