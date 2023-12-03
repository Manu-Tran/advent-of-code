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
n = 3
if not(filename):
    filename = "input.txt"
if filename == "input.txt":
    n = 9
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

print("Running with \"dry_run:{}\" ...".format(dry_run))

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    stacks = list()
    for i in range(n):
        stacks.append(deque())
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    flag = False
    for j,line in enumerate(arg) :
        for i in range(n):
           if (i*4 +1) >= len(line):
               break
           c = line[i*4+1]
           if c == "1":
              flag = True
              break
           if c != ' ':
              stacks[i].appendleft(c)
        if flag:
            break
    print(stacks)
    for k in range(j+2, len(arg)):
        line = arg[k]
        reg = re.match("move (\d+) from (\d+) to (\d+)", line)
        num = int(reg.group(1))
        fr = int(reg.group(2))-1
        to = int(reg.group(3))-1
        print(line, fr,to)
        for _ in range(num):
            if len(stacks[fr]) == 0:
                break
            a = stacks[fr].pop()
            stacks[to].append(a)
        print(stacks)
    print(stacks)
    return reduce(lambda a,b: a+b, [l[-1] if len(l) != 0 else "" for l in stacks], "")

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
