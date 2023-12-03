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

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.replace("\n\n", "\n").split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    st = deque()
    res = 0
    arg.append("[[2]]")
    arg.append("[[6]]")
    for i,v in enumerate(arg):
        arg[i] = eval(v)
    helper.blockPrint()
    arg.sort(key=cmp_to_key(compare), reverse=True)
    helper.enablePrint()
    print(arg)
    res = 1
    for i,v in enumerate(arg):
        if v == [[6]]:
            print(i+1)
            res *= i+1
        if v == [[2]]:
            res *= i+1
            print(i+1)
    return res

def compare(s1,s2):
    bs1 = isinstance(s1,list)
    bs2 = isinstance(s2,list)
    print("Comparing s1={} s2={}".format(s1,s2))
    if bs1 and bs2:
        print("list, list")
        last_i = 0
        for i in range(len(s1)):
            last_i = i
            if i == len(s2):
                print("Returning False not enough s2")
                return -1
            res = compare(s1[i], s2[i])
            if res == -1:
                print("Returning False greater than")
                return -1
            if res == 1:
                print("Returning True smaller than")
                return 1
        if len(s1) == len(s2):
            print("Returning Eq")
            return 0
        print("Returning True not enough s1")
        return 1
    elif not(bs1) and not(bs2):
        r = 0 if s1 == s2 else 1 if s1 < s2 else -1
        print("int, int")
        print("Returning r={}".format(r))
        return r
    elif not(bs1):
        print("int, list")
        r = compare([s1], s2)
        print("Returning r={}".format(r))
        return r
    elif not(bs2):
        print("list, int")
        r = compare(s1, [s2])
        print("Returning r={}".format(r))
        return r

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
