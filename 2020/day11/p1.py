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

@lru_cache
def get_voisins(x,y,x_max, y_max):
    res = []
    if x != 0:
        # 4
        res.append((x-1, y))
        if y != 0:
            # 1
            res.append((x-1, y-1))
        if y != (y_max-1):
            # 7
            res.append((x-1, y+1))
    if x != (x_max-1):
        if y != 0:
            # 3
            res.append((x+1, y-1))
        if y != (y_max-1):
            # 9
            res.append((x+1, y+1))
        # 6
        res.append((x+1, y))

    if y != 0:
        # 2
        res.append((x, (y-1)))
    if y != (y_max-1):
        # 8
        res.append((x, (y+1)))
    return res

def get_num_occupied(x,y,grid):
    voisins = get_voisins(x,y,len(grid), len(grid[0]))
    count = 0
    for v in voisins:
        if grid[v[0]][v[1]] == "#":
            count += 1
    return count


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    changes = []
    while True:
        change = False
        count = 0
        for i, line in enumerate(arg):
            new_line = []
            for j, c in enumerate(line):
                n = get_num_occupied(i,j, arg)
                if n == 0 and c == "L":
                    change=True
                    new_line.append("#")
                elif n >= 4 and c == "#":
                    change=True
                    new_line.append('L')
                else:
                    if c == "#":
                        count += 1
                    new_line.append(c)
            changes.append(new_line)
        arg = changes
        changes = []
        if not(change):
            return count

helper.blockPrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)
