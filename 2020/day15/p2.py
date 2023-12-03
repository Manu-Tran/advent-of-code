#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

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
    # argnum = list(map(int, arg))
    liste = arg[0].split(",")
    reg = defaultdict(lambda : [0,0])
    res = 0
    turn = 0
    for i in liste:
        turn += 1
        reg[int(i)][1] = (turn)
        res = int(i)
    pbar = tqdm(total=30000000)
    while turn < 100000:
        if turn%100 == 0:
            pbar.update(100)
        # print(turn)
        turn += 1
        # print(res, reg)
        # print(len(reg[res]))
        if (reg[res][0]) == 0:
            res = 0
        else:
            res = reg[res][-1] - reg[res][-2]
        reg[res][0] = reg[res][1]
        reg[res][1] = turn
        print(res)
    pbar.close()
    return res

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
