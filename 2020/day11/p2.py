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



def get_voisins(x,y,x_max,y_max, grid):
    @lru_cache
    def prolong(x,y, direction):
        while True:
            x += direction[0]
            y += direction[1]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return None
            if grid[x][y] != ".":
                return (x,y)
    @lru_cache
    def rec(x,y,x_max, y_max):
        res = []
        if x != 0:
            # 4
            a = prolong(x,y, (-1, 0))
            if a is not None:
                res.append(a)
            if y != 0:
                # 1
                a = prolong(x,y, (-1, -1))
                if a is not None:
                    res.append(a)
            if y != (y_max-1):
                # 7
                a = prolong(x,y, (-1, +1))
                if a is not None:
                    res.append(a)
        if x != (x_max-1):
            if y != 0:
                # 3
                a = prolong(x,y, (+1, -1))
                if a is not None:
                    res.append(a)
            if y != (y_max-1):
                # 9
                a = prolong(x,y, (+1, +1))
                if a is not None:
                    res.append(a)
            # 6
            a = prolong(x,y, (+1, 0))
            if a is not None:
                res.append(a)

        if y != 0:
            # 2
            a = prolong(x,y, (0, -1))
            if a is not None:
                res.append(a)
        if y != (y_max-1):
            # 8
            a = prolong(x,y, (0, +1))
            if a is not None:
                res.append(a)
        return res
    return rec(x,y,x_max, y_max)

def get_num_occupied(x,y,grid):
    voisins = get_voisins(x,y,len(grid), len(grid[0]), grid)
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
        test = ""
        for k in arg:
            line = ""
            for l in k:
                line += l
            test += line + "\n"
        print(test)
        # print(get_voisins(1,0,len(arg), len(arg[0]), arg))
        for i, line in enumerate(arg):
            new_line = []
            for j, c in enumerate(line):
                n = get_num_occupied(i,j, arg)
                if n == 0 and c == "L":
                    change = True
                    new_line.append("#")
                elif n >= 5 and c == "#":
                    change = True
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

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)
