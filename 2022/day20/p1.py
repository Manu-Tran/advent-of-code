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
from copy import copy

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
    argnum_old = list(map(int, arg))
    argnum = [(a,b) if b != 0 else (0,0) for a,b in enumerate(argnum_old)]
    org_order = copy(argnum)
    count = 0
    res = 0
    for n in org_order:
        reorder(n, argnum)
        count += 1
    print(len(argnum))
    print(argnum[(1000 + argnum.index((0,0)))%len(argnum)])
    print(argnum[(2000 + argnum.index((0,0)))%len(argnum)])
    print(argnum[(3000 + argnum.index((0,0)))%len(argnum)])
    res += argnum[(1000 + argnum.index((0,0)))%len(argnum)][1]
    res += argnum[(2000 + argnum.index((0,0)))%len(argnum)][1]
    res += argnum[(3000 + argnum.index((0,0)))%len(argnum)][1]
    return res

def reorder(x, liste):
    i = liste.index(x)
    liste.pop(i)
    j = (i + x[1])%(len(liste))
    while j < 0:
        j += (len(liste))
    liste.insert(j,  x)



if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
