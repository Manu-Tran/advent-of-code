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
    n = len(arg)
    res = 0
    for i in range(n//3):
        seen = set()
        line = arg[i*3]
        seen.update(line)
        line = arg[i*3+1]
        seen = seen.intersection(line)
        line = arg[i*3+2]
        seen = seen.intersection(line)
        print(seen)
        res += value(seen)

    return(res)

helper.enablePrint()
res = run()
helper.write_file(res)
print(res)

print("Done !")
