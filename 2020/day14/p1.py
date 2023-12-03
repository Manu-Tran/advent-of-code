#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *

import helper
import os
import sys
import re
import binascii

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

def applyMask(mask, value):
    n = len(mask)
    value = int(mask.replace("X", "1"), 2) & value

    return value




def run():
    mem = defaultdict(lambda _: 0)
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    mask = ""
    for line in arg:
        l = line.replace(" ", "").split("=")
        if l[0] == "mask":
            mask = l[1]
        else:
            match = re.match("mem\[(\d*)\]", l[0])
            mem[match.group(1)] = applyMask(mask, int(l[1]))
    res = 0
    for i in mem.keys():
        if mem[i] != 0 :
            res += mem[i]
    return res

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
