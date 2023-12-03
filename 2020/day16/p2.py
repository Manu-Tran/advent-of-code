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
    sums = 0
    to_remove = list()
    for t in tqdm(tickets):
        flag = False
        for v in t:
            vi = int(v)
            if not(any([any([vi >= int(r[0]) and vi <= int(r[1]) for r in c]) for c in classes.values()])):
                to_remove.append(t)
                break
    for t in to_remove:
        tickets.remove(t)

    print(tickets)
    res = defaultdict(lambda:list())
    for t in tqdm(tickets):
        flag = False
        for i,v in enumerate(t):
            vi = int(v)
            flag = False
            found_count = 0
            found = ""
            for cl in classes:
                c = classes[cl]
                for r in c:
                    if (vi >= int(r[0]) and vi <= int(r[1])):
                        print(vi, r)
                        res[cl].append(i)


    max_i = 0
    max_v = 0
    trueres = defaultdict(lambda:list())
    for cl in tqdm(res):
        max_i = 0
        max_v = 0
        for i in range(len(classes)):
            if res[cl].count(i) == len(tickets):
                trueres[cl].append(i)

    final = dict()
    while len(final) != len(classes):
        for cl in trueres:
            if len(trueres[cl]) == 1:
                i = trueres[cl][0]
                final[cl] = i
                for cli in trueres:
                    try:
                        trueres[cli].remove(i)
                    except ValueError:
                        continue
    print(final)
    print(trueres)
    print(res)

    prd = 1
    print(trueres)
    for cl in tqdm(final):
        print("class", cl)
        print(final[cl])
        if "departure" in cl:
            print(ticket[final[cl]])
            prd *= int(ticket[final[cl]])
    return prd

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
