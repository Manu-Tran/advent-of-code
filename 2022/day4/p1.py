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
dry_run = not(bool(os.getenv("SUBMIT", "False")))

print("Running ...")

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    sums = 0
    for line in arg:
        r = line.split(",")
        r1 = r[0].split("-")
        r2 = r[1].split("-")
        range1 = set(range(int(r1[0]), int(r1[1])+1))
        range2 = set(range(int(r2[0]), int(r2[1])+1))
        if range1.issubset(range2) or range2.issubset(range1):
            sums += 1
    return sums

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
print(res)

print("Done !")
