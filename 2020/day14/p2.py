#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *

import helper
import os
import sys
import re
import binascii
import copy

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

def applyMask(mask, value,res):
    n = len(mask)
    if mask == "":
        sets = set()
        sets.add(int(res, 2))
        print(res)
        print(int(res,2))
        return sets
    x = mask[0]
    if x == "X":
        # print(value, mask)
        return applyMask(mask[1:], value[1:], res+"1").union(applyMask(mask[1:], value[1:], res+"0"))
    if x == "0":
        # print(value, mask)
        return applyMask(mask[1:], value[1:], res+value[0])
    if x == "1":
        # print(value, mask)
        return applyMask(mask[1:], value[1:], res+"1")


def pad(x, n):
    return "0"*(n-len(x)) + x



def run():
    seen = set()
    mem = defaultdict(lambda _: 0)
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    mask = ""
    buff = ""
    for i, line in enumerate(arg) :
        if "mask =" in line:
            if buff == "":
                buff = line
            else:
                tmp = buff
                buff = line
                arg[i] = tmp
    arg.append(buff)
    sums = 0
    for line in reversed(arg):
        print(line)
        l = line.replace(" ", "").split("=")
        if l[0] == "mask":
            mask = l[1]
        else:
            match = re.match("mem\[(\d*)\]", l[0])
            values = applyMask(mask, pad(bin(int(match.group(1)))[2:], 36), "")
            sums += len(values.difference(seen))*int(l[1])
            seen.update(values)
    return sums


if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
