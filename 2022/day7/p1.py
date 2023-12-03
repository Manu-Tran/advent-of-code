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
sys.setrecursionlimit(3000)


print("Running with \"dry_run:{}\" ...".format(dry_run))

def get_pwd(paths):
    print(paths)
    return reduce(lambda x,y:x+"."+y, paths, "")

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    res = defaultdict(lambda:dict())
    cur_dir = "/"
    dir_stack = deque()
    ls_flag = False
    cur_dir_folder = None
    for line in arg:
        print(line)
        cmd = line.split()
        if cmd[0] == "$":
            ls_flag = False
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    t = dir_stack.pop()
                    cur_dir = get_pwd(dir_stack)
                else:
                    dir_stack.append(cmd[2])
                    cur_dir = get_pwd(dir_stack)
            elif cmd[1] == "ls":
                ls_flag = True
        elif ls_flag:
            if cmd[0] == "dir":
                res[cur_dir][cmd[1]] = "dir"
            else:
                print(cur_dir)
                res[cur_dir][cmd[1]] = int(cmd[0])
    print(res)
    print("END")
    mega = find_size(res,"./")
    a = list(mega.values())
    a.sort()
    print(a)
    b = list(filter(lambda x : x <= 100000, a))
    print(b)
    return sum(b)

def find_size(system, f):
    mega = dict()
    def rec(system, f):
        size = 0
        for c in system[f]:
            d = system[f][c]
            if (isinstance(d, int)):
                size += d
                print(d)
            else:
                print(f+"."+c)
                size += rec(system, f+ "." +c)
        print(f)
        print(size)
        mega[f] = size
        return size
    rec(system,f)
    return mega

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
