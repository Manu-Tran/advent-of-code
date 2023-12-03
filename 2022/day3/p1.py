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

print("Running ...")

def value(c):
    c = next(iter(c))
    if c.islower():
        return ord(c)-96
    else:
        return ord(c)-64+26

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    sums = list()
    for line in arg:
        n = len(line)
        s1 = set(line[:(n//2)])
        s2 = set(line[(n//2):])
        both = s1.intersection(s2)
        sums.append(both)
    # argnum = list(map(int, arg))
    res =0
    print(list(map(lambda x: value(x), sums)))
    for c in sums:
        res += value(c)
    return(res)

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
