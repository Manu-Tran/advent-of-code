#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

import numpy as np
import re
import helper
import os
from dijkstar import Graph, find_path
import copy
import bisect

# >>> graph = Graph()
# >>> graph.add_edge(1, 2, 110)
# >>> graph.add_edge(2, 3, 125)
# >>> graph.add_edge(3, 4, 108)
# >>> find_path(graph, 1, 4)
# PathInfo(
#     nodes=[1, 2, 3, 4],
#     edges=[110, 125, 108],
#     costs=[110, 125, 108],
#     total_cost=343)

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

def get_voisins(x,y, grid):
    res = set()
    n_x = len(grid)
    n_y = len(grid[0])
    if x != n_x-1:
        res.add((x+1,y))
    if y != n_y-1:
        res.add((x,y+1))
    if x != 0:
        res.add((x-1,y))
    if y != 0:
        res.add((x,y-1))
    return res

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    n = len(arg)
    m = len(arg[0])
    start =None
    end = None
    starts = list()
#  [1, 2, 4, 5]
# bisect.insort(a, 3)
    for i,line in enumerate(arg):
        for j,c in enumerate(line):
            if c == "S":
                arg[i] = arg[i].replace("S",'a')
                start = (i,j)
                starts.append(start)
            elif c == "E":
                end = (i,j)
                arg[i] = arg[i].replace("E",'z')
            elif c == "a":
                start = (i,j)
                starts.append(start)
    megamini = float("inf")
    for start in starts:
        dj = dict()
        seen = set()
        dj = defaultdict(lambda:float('inf'))
        dj[start] = 0
        seen.add(start)
        voisin = set()
        voisin.add(start)
        while len(voisin) != 0:
            # print(seen)
            print(voisin)
            v = None
            mini = float("inf")
            for c in voisin:
                if v == None:
                    v = c
                    mini = dj[v]
                elif mini > dj[c]:
                    v = c
                    mini = dj[c]
            voisin.remove(v)
            seen.add(v)
            for b in get_voisins(*v, arg):
                if b not in seen and reachable(v,b,arg):
                    dj[b] = min(dj[v] + 1, dj[b])
                    voisin.add(b)
        if dj[end] < megamini:
            megamini = dj[end]
    return megamini

def reachable(deb, tar, grid):
    return (ord(grid[tar[0]][tar[1]]) - ord(grid[deb[0]][deb[1]])) <= 1

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
