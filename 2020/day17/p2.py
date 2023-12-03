#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

import re
import helper
import os
import sys

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

@lru_cache
def get_neighbors(pos):
    voisins = set()
    for x in [-1,0,+1]:
        for y in [-1,0,+1]:
            for z in [-1,0,+1]:
                for w in [-1,0,+1]:
                    if x != 0 or y != 0 or z != 0 or w != 0:
                        voisins.add((pos[0]+x,pos[1]+y,pos[2]+z, pos[3]+w))
    return voisins

def one(pos, i):
    if i == 0:
        return((pos[0]+1, pos[1], pos[2], pos[3]))
    elif i == 1:
        return((pos[0], pos[1]+1, pos[2], pos[3]))
    elif i == 2:
        return((pos[0], pos[1], pos[2]+1, pos[3]))
    else:
        return((pos[0], pos[1]+1, pos[2], pos[3] + 1))

def count_active(pos, sparses):
    count = 0
    for v in get_neighbors(pos):
        if v in sparses:
            count += 1
    return count

def step(sparses):
    to_activate = set()
    to_deactivate = set()
    for s in sparses:
        vois = get_neighbors(s)
        if not(count_active(s, sparses) in [2,3]):
            to_deactivate.add(s)
        for v in vois:
            if not(v in sparses):
               if count_active(v, sparses) == 3:
                   to_activate.add(v)
    return sparses.union(to_activate).difference(to_deactivate)




def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    sparses = set()
    for x,line in enumerate(arg):
        for y,i in enumerate(line):
            if i == "#":
                sparses.add((x,y,0,0))
    for i in range(6):
        sparses = step(sparses)
    return len(sparses)

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
