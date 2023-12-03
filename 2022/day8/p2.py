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

    dist = defaultdict(lambda:1)
    maxi =0
    for i in range(1,n-1):
        for j in range(1,n-1):
            dist[(i,j)] = view(i,j,arg)
            maxi = max(maxi, dist[(i,j)])
    count = 0
    s = ""
    max_sum = 0
    sums = 0
    x = ""
    for i in range(n):
        for j in range(n):
            x += " 0" + str(dist[(i,j)]) if dist[(i,j)] < 10 else " " + str(dist[(i,j)])
            if grid[(i,j)]:
                sums += 1
                s += "1"
                count += 1
            else:
                s += "0"
        s+="\n"
        x+="\n"
    print(s)
    print(x)
    # print(grid)
    return max([max([dist[(i,j)] for i in range(n)]) for j in range(n)])

def view(i_start,j_start, arg):
    ref = int(arg[i_start][j_start])
    @lru_cache(maxsize=None)
    def rec(i,j, direc, max_size):
        n = len(arg)
        # print(i,j)
        k = int(arg[i][j])
        if direc == 0:
            seen = 1
            # if (k >= max_size):
            #     seen = 1
            if i == 0 or k >= ref:
                return seen
            else:
                a = rec(i-1,j,direc,max(k,max_size))
                return seen + a
        elif direc == 1:
            seen = 1
            # if (k >= max_size):
            #     seen = 1
            if j == n-1 or k >= ref:
                return seen
            else:
                a = rec(i,j+1,direc,max(k,max_size))
                return seen + a

        elif direc == 2:
            seen = 1
            # if (k >= max_size):
            #     seen = 1
            if i == n-1 or k >= ref:
                return seen
            else:
                a = rec(i+1,j,direc,max(k,max_size))
                return seen + a

        elif direc == 3:
            seen = 1
            # if (k >= max_size):
            #     seen = 1
            if j == 0 or k >= ref:
                return seen
            else:
                a = rec(i,j-1,direc,max(k,max_size))
                return seen + a

    return (rec(i_start-1,j_start,0, 0)
            * rec(i_start+1,j_start,2, 0)
            * rec(i_start,j_start+1,1, 0)
            * rec(i_start,j_start-1,3, 0))


if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
