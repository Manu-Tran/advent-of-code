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

def slope(vector, grid):
    res = 0
    tree = 0
    x_pos, y_pos = 0, 0
    while x_pos != len(grid):
        if grid[x_pos][y_pos] == "#":
            tree += 1
        x_pos += vector[0]
        y_pos += vector[1]
        y_pos %= len(grid[0])
    return tree


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    return slope((1,3), arg)

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)
