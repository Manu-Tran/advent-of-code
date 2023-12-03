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
    sched = defaultdict(lambda:[])
    signal = 1
    time = 0
    res = []
    line = arg[0]
    counter = 0
    while True:
        print(line)
        l = line.split()
        if l[0] == "addx":
            v = int(l[1])
            time += 1
            if time in [20,60,100,140,180,220]:
                res.append(time*signal)
                print(time,signal)
                if time == 220:
                    print(res)
                    return sum(res)
            time += 1
            if time in [20,60,100,140,180,220]:
                res.append(time*signal)
                print(time,signal)
                if time == 220:
                    print(res)
                    return sum(res)
            signal += v
        if l[0] == "noop":
            time += 1
            if time in [20,60,100,140,180,220]:
                res.append(time*signal)
                print(time,signal)
                if time == 220:
                    print(res)
                    return sum(res)
        counter += 1
        line = arg[counter % len(arg)]
    return None

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
