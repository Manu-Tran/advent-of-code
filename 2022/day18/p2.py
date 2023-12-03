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

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))

def get_voisins(c):
    res = set()
    res.add((c[0]+1, c[1], c[2]))
    res.add((c[0]-1, c[1], c[2]))
    res.add((c[0], c[1]+1, c[2]))
    res.add((c[0], c[1]-1, c[2]))
    res.add((c[0], c[1], c[2]+1))
    res.add((c[0], c[1], c[2]-1))
    return res

def get_voisins_max(c, c_max, c_min):
    rs = set()
    if (c_min[0] -1 < c[0]):
        rs.add((c[0]-1, c[1], c[2]))
    if (c_max[0] +1 > c[0]):
        rs.add((c[0]+1, c[1], c[2]))
    if (c_min[1] -1 < c[1]):
        rs.add((c[0], c[1]-1, c[2]))
    if (c_max[1] +1 > c[1]):
        rs.add((c[0], c[1]+1, c[2]))
    if (c_min[2] -1 < c[2]):
        rs.add((c[0], c[1], c[2]-1))
    if (c_max[2] +1 > c[2]):
        rs.add((c[0], c[1], c[2]+1))
    return rs


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    cubes = set()
    max_x,max_y,max_z = 0,0,0
    min_x,min_y,min_z = float('inf'), float('inf'), float('inf')
    for line in arg:
        l = line.split(",")
        cube = tuple(map(int, l))
        cubes.add(cube)
        if cube[0] > max_x:
            max_x = cube[0]
        if cube[0] < min_x:
            min_x = cube[0]
        if cube[1] > max_y:
            max_y = cube[1]
        if cube[1] < min_y:
            min_y = cube[1]
        if cube[2] > max_z:
            max_z = cube[2]
        if cube[2] < min_z:
            min_z = cube[2]
    maxes = (max_x,max_y,max_z)
    mines = (min_x,min_y,min_z)

    clusters = list()
    count = 0
    for c in cubes:
        for v in get_voisins(c):
            if v not in cubes:
                found = False
                for cl in clusters:
                    if v in cl:
                        found = True
                        break
                if not found:
                    # print(v)
                    res = set()
                    res.add(v)
                    clusters.append(add_to_cluster(v, res, set(), maxes, mines, cubes))
    # print(clusters)
    max_length =  sorted(list(map(len, clusters)))[-1]

    count = 0
    for c in cubes:
        for v in get_voisins(c):
            if v not in cubes:
                count += 1
    print(count)
    for cl in clusters:
        if len(cl) == max_length:
            continue
        else:
            for c in cl:
                for v in get_voisins(c):
                    if v not in cl:
                        count -= 1
    return count

def add_to_cluster(cube, res, ss, maxes, mines, cubes):
    ss.add(cube)
    # print(cube, get_voisins_max(cube, maxes,mines))
    for v in get_voisins_max(cube, maxes, mines):
        if (v not in cubes) and (v not in ss):
            # print(cube,v)
            res.add(v)
            res.update(add_to_cluster(v, res, ss, maxes, mines, cubes))
            # print()
    return res


if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
