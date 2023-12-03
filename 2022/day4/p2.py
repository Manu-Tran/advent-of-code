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
        if len(range1.intersection(range2)) != 0:
            sums += 1
    return sums

res = run()
helper.write_file(res)
print(res)

print("Done !")
