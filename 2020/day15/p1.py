#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *

import helper
import os
import sys

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")
#436
def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    liste = arg[0].split(",")
    reg = defaultdict(lambda : list())
    res = 0
    turn = 0
    for i in liste:
        turn += 1
        reg[int(i)].append(turn)
        res = int(i)
    while turn < 2020:
        # print(turn)
        turn += 1
        # print(res, reg)
        # print(len(reg[res]))
        if len(reg[res]) == 1:
            res = 0
        else:
            res = reg[res][-1] - reg[res][-2]
        reg[res].append(turn)
    return res

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
