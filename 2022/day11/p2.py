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

def lbda(x, line):
    n = line.replace("old", str(x))
    return eval(n)


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    w_level = 0
    monkeys = dict()
    monkey = dict()
    i = 0
    while i <= (len(arg)):
        line = arg[i]
        l = line.split()
        monkey["id"] = l[1][:-1]
        print(monkey["id"])
        i += 1
        line = arg[i]
        l = line.split()
        monkey["item"] = deque()
        for c in l[2:]:
            monkey["item"].append(int(c.replace(',', "")))
        print(monkey["item"])
        i += 1
        line = arg[i]
        l = line.split()
        print(l)
        monkey["cmd"] = str(reduce(lambda x,y: x+" "+y, l[3:], ""))
        print(monkey["cmd"])
        monkey["op"] = lambda x,cmd : eval(cmd.replace("old", str(x)))
        i += 1
        line = arg[i]
        l = line.split()
        monkey["test"] = int(l[3])
        print(monkey["test"])
        i += 1
        line = arg[i]
        l = line.split()
        monkey[True] = l[5]
        print(monkey[True])
        i += 1
        line = arg[i]
        l = line.split()
        monkey[False] = l[5]
        print(monkey[False])
        i+= 2
        monkeys[monkey["id"]] = monkey
        monkey = dict()
    # argnum = list(map(int, arg))
    count = defaultdict(lambda:0)
    for _ in tqdm(range(10000)):
        round(monkeys, count)
    res = sorted(count.values())[-2:]
    print(count.values())
    print(res)
    return res[0]*res[1]

def round(monkeys, count):
    ppcm = 1
    for m in monkeys.values():
        ppcm *= m["test"]
    for idm in monkeys:
        print("Monkey {}".format(idm))
        monkey = monkeys[idm]
        n = len(monkey["item"])
        for i in range(n):
            it = monkey["item"].popleft()
            it = monkey["op"](it, monkey["cmd"])
            test = (it % monkey["test"]) == 0
            nextm = monkey[test]
            next_monkey = monkeys[nextm]
            monkeys[nextm]["item"].append(it % ppcm)
            count[monkey["id"]] += 1
            print("Sending {} to monkey {}".format(it, nextm))

if not(dry_run):
    helper.blockPrint()
else:
    # helper.enablePrint()
    helper.blockPrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
