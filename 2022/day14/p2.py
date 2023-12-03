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
    border = defaultdict(lambda:".")
    max_x = 0
    for line in arg:
        print(line)
        last_pos = None
        pos = None
        for l in line.split(" -> "):
            last_pos = pos
            print(l)
            p = l.split(',')
            pos = (int(p[0]), int(p[1]))
            print(pos)
            if pos[1] > max_x:
                max_x = pos[1]
            if last_pos == None:
                continue
            if last_pos[0] != pos[0] and last_pos[1] == pos[1]:
                for i in range(min(last_pos[0], pos[0]), max(last_pos[0], pos[0])+1):
                    border[(i, pos[1])] = "#"
            elif last_pos[0] == pos[0] and last_pos[1] != pos[1]:
                for i in range(min(last_pos[1], pos[1]), max(last_pos[1], pos[1])+1):
                    border[(pos[0], i)] = "#"
            else :
                print("yolo")
    start = (500,0)
    cont = True
    count = 0
    while cont:
        y,x = start[0], start[1]
        while True:
            if x > (max_x+10):
                cont = False
                break
            while border[(y,x+1)] == "." and (x+1 < max_x+2) :
                if x > (max_x+10):
                    cont = False
                    break
                x += 1
            # print("max = ", max_x+2)
            # print(x,y)
            print(border[(y+1,x+1)])
            print(border[(y-1,x+1)])
            if not(cont):
                break
            if border[(y-1,x+1)] == "." and (x+1 < max_x+2):
                x += 1
                y -= 1
            elif border[(y+1,x+1)] == "." and (x+1 < max_x+2):
                x += 1
                y += 1
            else:
                break
        if cont:
            print(x,y)
            border[(y,x)] = "o"
            count += 1
            if (x == 0):
                break
    # s = ""
    # for j in range(0,14):
    #     for i in range(480,510):
    #         s += border[(i,j)]
    #     s+= "\n"
    # print(s)
    return count


if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
