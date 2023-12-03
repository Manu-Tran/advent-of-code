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

print("Running with \"dry_run:{}\" ...".format(dry_run))

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    p1 = deque()
    for line in arg[0].split('\n')[1:]:
        p1.append(int(line))
    p2 = deque()
    for line in arg[1].split('\n')[1:]:
        if line:
            p2.append(int(line))
    while len(p1) != 0 and len(p2) != 0:
        print(p1, p2)
        a = p1.popleft()
        b = p2.popleft()
        if a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    if len(p1)==0:
        return score(p2)
    else:
        return score(p1)

def score(deck):
    score = 0
    for i,k in enumerate(deck):
        score += k * (len(deck) - i)
    return score

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
