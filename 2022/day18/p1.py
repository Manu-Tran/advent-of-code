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

def get_voisins(c):
    res = set()
    res.add((c[0]+1, c[1], c[2]))
    res.add((c[0]-1, c[1], c[2]))
    res.add((c[0], c[1]+1, c[2]))
    res.add((c[0], c[1]-1, c[2]))
    res.add((c[0], c[1], c[2]+1))
    res.add((c[0], c[1], c[2]-1))
    return res

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    cubes = set()
    for line in arg:
        l = line.split(",")
        cube = tuple(map(int, l))
        cubes.add(cube)
    count = 0
    for c in cubes:
        for v in get_voisins(c):
            if v not in cubes:
                count += 1
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
