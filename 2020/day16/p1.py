#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

import helper
import os
import sys
import re

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    line = arg[0]
    count = 0
    classes = defaultdict(lambda:[])
    while line != "":
        # print(line)
        match = re.match("(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
        classes[match.group(1)].append(
            (int(match.group(2)), int(match.group(3))))
        classes[match.group(1)].append(
            (int(match.group(4)), int(match.group(5))))
        count += 1
        line = arg[count]
    count += 2
    ticket = arg[count].split(",")
    count += 3
    tickets = []
    while count != len(arg):
        line = arg[count]
        tickets.append(line.split(','))
        count += 1
    print(classes)
    # argnum = list(map(int, arg))
    for t in tickets:
        flag = False
        for v in t:
            vi = int(v)
            if not(any([any([vi >= int(r[0]) and vi <= int(r[1]) for r in c]) for c in classes.values()])):
                print(vi)
                sums += vi
                flag = True
                break
    return sums

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
