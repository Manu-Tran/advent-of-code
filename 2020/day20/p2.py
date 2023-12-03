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

M = 3
if filename == "input.txt":
   M = 12

print("Running ...")
N = 10

#    0
#  3   1
#    2

def fuse(t1,t2, d1):
    if d1 == 1:
        return t2 + t1
    elif d1 == 2:
        return [x + y  for x,y in zip(t1,t2)]
    elif d1 == 3:
        return t1 + t2
    elif d1 == 4:
        return [x + y  for x,y in zip(t2,t1)]

def reverse(t):
    return [reversed(x) for x in t]

def rot90(m):
    return list(zip(*reversed(m)))

def get_rev_edges(t):
    res = set()
    res.add(tuple(reversed(t[0])))
    res.add(tuple(reversed(t[-1])))

    # print(t)
    tp = list(zip(*t))
    # print(tp)
    res.add(tuple(reversed(tp[0])))
    res.add(tuple(reversed(tp[-1])))
    return res

def remove_edges(t):
    return list(zip(*(list(zip(*(t[1:-1])))[1:-1])))

def get_edges(t):
    res = list()
    tp = list(zip(*t))
    res.append(tuple(t[0]))
    res.append(tuple(tp[-1]))
    res.append(tuple(t[-1]))
    res.append(tuple(tp[0]))
    return res

SEEN = set()

def build_tab(cur_id, d1, voisins, tiles, edges, corner):
    res = list()
    print("id", cur_id)
    print("dir", d1)
    print(voisins[cur_id])
    for v in voisins[cur_id]:
        print(v,edges[(cur_id, v)])
        for d in edges[(cur_id, v)]:
            if d1 == d[0]:
                if v in corner and v not in SEEN:
                    print("v",v)
                    SEEN.add(v)
                    print("corner FOUND")
                    if d[1] < 0 :
                        return remove_edges(reverse(tiles[v]))
                    else:
                        return remove_edges(tiles[v])
                else:
                    print("v",v)
                    SEEN.add(v)
                    if d[1] < 0 :
                        t = build_tab(v, d1, voisins, tiles, edges, corner)
                        if t != None:
                            return fuse(remove_edges(reverse(tiles[v])), t, d1)
                        else:
                            return remove_edges(reverse(tiles[v]))
                    else:
                        t = build_tab(v, d1, voisins, tiles, edges, corner)
                        if t != None:
                            return fuse(remove_edges(tiles[v]), t, d1)
                        else:
                            return remove_edges(tiles[v])

def run():
    seen_edges = set()
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    tiles = list()
    tiles_dict = dict()
    for tile in arg:
        t = tile.split("\n")
        tile_id = int(t[0][5:-1])
        tiles.append((tile_id,list(filter(lambda x: x != "", t[1:]))))
        tiles_dict[tile_id] = list(filter(lambda x: x != "", t[1:]))
    res_dict = defaultdict(lambda: set())
    edges = defaultdict(lambda:[])
    for id1,t1 in tiles:
        for id2,t2 in tiles:
            if id1 != id2:
                for i,v1 in enumerate(get_edges(t1)):
                    for j,v2 in enumerate(get_edges(t2)):
                        if v1 == v2:
                            edges[(id1,id2)].append((i+1,j+1))
                if len(edges[(id1,id2)]) == 0:
                    for i,v1 in enumerate(get_edges(t1)):
                        for j,v2 in enumerate(get_rev_edges(t2)):
                            if v1 == v2:
                                edges[(id1,id2)].append((i+1,-j-1))
                if len(edges[(id1,id2)]) != 0:
                    res_dict[id1].add(id2)
                    res_dict[id2].add(id1)
    res = 1
    corner = list()
    border = list()
    center = list()
    print(res_dict)
    for i in res_dict.keys():
        if len(res_dict[i]) == 4:
            center.append(i)
        elif len(res_dict[i]) == 2:
            corner.append(i)
        elif len(res_dict[i]) == 3:
            border.append(i)
    print(corner)
    #################################""
    id1 = corner[0]
    vois = iter(res_dict[id1])
    cur_v = next(vois)
    finalboard = None
    direc = edges[id1, cur_v][0]
    d1 = abs(direc[0])
    d2 = edges[(id1, next(vois))][0]
    vois = iter(res_dict[id1])
    cur_v = next(vois)
    while vois not in corner:
        SEEN.add(id1)
        c = (fuse(remove_edges(tiles_dict[id1]), build_tab(cur_v, d1, res_dict, tiles_dict, edges, corner), d1))
        if finalboard:
            finalboard = fuse(finalboard,c,d2)
        else:
            finalboard = c
        id1 = next(vois)
        vois = iter(res_dict[id1])
        cur_v = next(vois)
    c = (fuse(remove_edges(tiles_dict[id1]), build_tab(cur_v, d1, res_dict, tiles_dict, edges, corner), d1))
    finalboard = fuse(finalboard,c,d2)

    string = ""
    for line in finalboard:
        for c in line:
            string += c
        string += "\n"

    print(string)
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
