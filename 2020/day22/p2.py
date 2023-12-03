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
import copy

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))

mega_dict = dict()

print(filename)
def round(p1, p2, seen_conf):
    hash_list = str(p1)+str(p2)
    if len(p1) == 0:
        print("p2 win")
        return "p2"
    if len(p2) == 0:
        print("p1 win")
        return "p1"
    if (hash_list) in seen_conf:
        return "p1"
    seen_conf.add(hash_list)
    print(p1, p2)
    a = p1.popleft()
    b = p2.popleft()
    print("playing {} {}".format(a,b))
    if a <= len(p1) and b <= len(p2):
        new_p1 = copy.copy(p1)
        new_p2 = copy.copy(p2)
        print("start recursive game")
        res = round(new_p1, new_p2, set())
        if res == "p1":
            p1.append(a)
            p1.append(b)
        else :
            p2.append(b)
            p2.append(a)
        return round(p1,p2, seen_conf)
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)
    return round(p1,p2, seen_conf)

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    p1 = deque()
    for line in arg[0].split('\n')[1:]:
        p1.append(int(line))
    p2 = deque()
    seen_conf = set()
    for line in arg[1].split('\n')[1:]:
        if line:
            p2.append(int(line))
    res = round(p1,p2, set())
    if res == "p2":
        return score(p2)
    else:
        return score(p1)

def score(deck):
    score = 0
    for i,k in enumerate(deck):
        score += k * (len(deck) - i)
    return score

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
