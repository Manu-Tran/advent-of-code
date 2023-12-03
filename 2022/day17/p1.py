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

blocs = [
    {"shape": [(0, 0), (0, 1), (0, 2), (0, 3)], "height" : 0, "width": 3},
    {"shape": [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], "height" : 2, "width": 2},
    {"shape": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], "height" : 2, "width": 2},
    {"shape": [(0, 0), (1, 0), (2, 0), (3, 0)], "height" : 3, "width": 0},
    {"shape": [(0, 0), (0, 1), (1, 0), (1, 1)], "height" : 1, "width": 1},
    ]

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))

def run():
    f = open(filename, "r")
    f = f.read()
    max_height = 0
    arg = f.replace("\n", "")
    grid = deque()
    cur_pos = [3,2]
    for i in range(4):
        grid.append(["."]*7)
    s_p = 0
    bloc = blocs[s_p]
    count =0
    s_c = 0
    bar = tqdm(total=2022)
    while True:
        c = arg[s_c%len(arg)]
        s_c += 1
        if c == ">":
            if cur_pos[1] + bloc["width"] < 6 and check_space(grid, (cur_pos[0], cur_pos[1]+1), bloc):
                cur_pos[1] += 1
                # print("right one ", cur_pos)
        else:
            if cur_pos[1] > 0 and check_space(grid, (cur_pos[0], cur_pos[1]-1), bloc):
                cur_pos[1] -= 1
                # print("left one ", cur_pos)
        check_below = check_space(grid, (cur_pos[0]-1, cur_pos[1]), bloc)
        if check_below:
            cur_pos[0] -= 1
            # print("down one ", cur_pos)
        else:
            bar.update(1)
            for s in bloc["shape"]:
                # print(bloc)
                y,x = (cur_pos[0]+s[0], cur_pos[1] + s[1])
                grid[y][x] = "#"
                # print(y,x)
            # print(cur_pos, bloc, max_hejght)
            max_height = max(cur_pos[0] + bloc["height"]+1, max_height)
            reset_y_pos = max_height + 3
            padding = reset_y_pos - len(grid) + 4
            for _ in range(0, padding):
                grid.append(["."]*7)
            s_p += 1
            bloc = blocs[s_p%len(blocs)]
            cur_pos = [reset_y_pos,2]
            count += 1
        if count == 2022:
            break
    grid.reverse()
    print_grid(grid)
    return max_height

def print_grid(grid) :
    s = ""
    for line in grid:
        for c in line:
            s += c
        s += "\n"
    print(s)

def check_space(grid, pos, bloc):
    free = True
    if pos[0] == -1:
        return False
    for s in bloc["shape"]:
        y,x = (pos[0]+s[0], pos[1] + s[1])
        # print(y,x,len(grid))
        if grid[y][x] != ".":
            free = False
    return free


if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
