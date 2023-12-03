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

print("Running ...")
N = 10

def rot90(m):
    return list(zip(*reversed(m)))

def get_edges(t):
    res = set()
    res.add(tuple(t[0]))
    res.add(tuple(t[-1]))
    res.add(tuple(reversed(t[0])))
    res.add(tuple(reversed(t[-1])))

    # print(t)
    tp = list(zip(*t))
    # print(tp)
    res.add(tuple(tp[0]))
    res.add(tuple(tp[-1]))
    res.add(tuple(reversed(tp[0])))
    res.add(tuple(reversed(tp[-1])))
    return res

def run():
    seen_edges = set()
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    tiles = list()
    for tile in arg:
        t = tile.split("\n")
        tile_id = int(t[0][5:-1])
        tiles.append((tile_id,list(filter(lambda x: x != "", t[1:]))))
    # print(get_edges(tiles[0][1]))
    res_dict = defaultdict(lambda: 0)
    for id1,t1 in tiles:
        for id2,t2 in tiles:
            if id1 != id2:
                inter = len(get_edges(t1) & get_edges(t2))
                if (inter):
                    res_dict[id1] += 1
                    # print(id1, id2)
                    # print(inter)
    res = 1
    for i in res_dict.keys():
        if res_dict[i] == 2:
            res *= i
            print(i)
    print(res_dict)
    return res
    # return arg

# if filename == "input.txt":
#     helper.blockPrint()
res = run()
helper.write_file(res)
# if filename == "input.txt":
#     helper.enablePrint()
print(res)

print("Done !")
