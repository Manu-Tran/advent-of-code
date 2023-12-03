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
    res = dict()
    for line in arg:
        ope = re.match("(....): (....) (.) (....)", line)
        assign = re.match("(....): (\d+)", line)
        if assign != None:
            res[assign.group(1)] = int(assign.group(2))
        elif ope != None:
            res[ope.group(1)] = [ope.group(2), ope.group(3), ope.group(4)]
    return compute(res)

def is_computed(instr, x):
    return isinstance(instr[x], int)

def compute(instr, cur="root"):
    if is_computed(instr, cur):
        return instr[cur]
    else:
        x = compute(instr, instr[cur][0])
        op = instr[cur][1]
        y = compute(instr, instr[cur][2])
        r = int(eval(str(x) + op + str(y)))
        return r



if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
