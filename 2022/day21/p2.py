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
from copy import deepcopy

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
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    res = dict()
    for line in arg:
        ope = re.match("(....): (....) (.) (....)", line)
        assign = re.match("(....): (\d+)", line)
        if assign != None:
            res[assign.group(1)] = int(assign.group(2))
        elif ope != None:
            res[ope.group(1)] = [ope.group(2), ope.group(3), ope.group(4)]
    i = 0
    # print(res)
    # print(res["root"])
    comp = dict()
    for op in res:
        comp[op] = is_computable(res, op)
    # print(comp)

    a,_,b = res["root"]
    new_res = deepcopy(res)
    invert_eq(res, comp, "humn", new_res)
    # print(new_res)

    if comp[a]:
        new_res[a] = res[b]
        new_res[b] = compute(res, a)
    else:
        new_res[b] = res[a]
        new_res[a] = compute(res, b)

    print("yolo")
    print(new_res["root"])
    f = compute(new_res, "humn")
    if comp[a]:
        print(compute(res, a))
        print(compute(res, b, f))
    else:
        print(compute(res, b))
        print(compute(res, a, f))
    # print(new_res)
    return f

    # while not(compute(res, "root", i)):
    #     i += 1
    return i

def is_computable(instr, cur):
    if cur == "humn":
        return False
    if is_computed(instr, cur):
        return True
    else:
        x = is_computable(instr, instr[cur][0])
        y = is_computable(instr, instr[cur][2])
        return x and y

def invert_op(op, a, y, y_first):
    if op =="*":
        return [y, "/", a]
    elif op == "+":
        return [y, "-", a]
    elif op == "-":
        if y_first:
            return [y, "+", a]
        else:
            return [a, "-", y]
    elif op == "/":
        if y_first:
            return [y, "*", a]
        else:
            return [a, "/", y]

SEEN = set()
def invert_eq(instr, comp, x, new_res):
    if comp[x]:
        return
    if is_computed(instr, x) and x != "humn":
        return
    op1, op2 = None, None
    SEEN.add(x)
    for y in instr:
        if is_computed(instr, y) :
            continue
        if y in SEEN:
            continue
        if x in instr[y] and not(comp[y]):
            if instr[y][0] == x:
                other = instr[y][2]
                new_res[x] = invert_op(instr[y][1], instr[y][2], y, True)
                op1, op2 = y, instr[y][2]
                invert_eq(instr, comp, op1, new_res)
                invert_eq(instr, comp, op2, new_res)
            else:
                other = instr[y][0] if instr[y][0] != x else instr[y][2]
                new_res[x] = invert_op(instr[y][1], instr[y][0], y, False)
                op1, op2 = y, instr[y][0]
                invert_eq(instr, comp, op1, new_res)
                invert_eq(instr, comp, op2, new_res)

def is_computed(instr, x):
    return isinstance(instr[x], int)

def compute(instr, cur="root", humn=0):
    # print(cur)
    # print(instr[cur])
    if humn != 0 and cur == "humn":
        return humn
    if cur == "root":
        x = compute(instr, instr[cur][0], humn)
        y = compute(instr, instr[cur][2], humn)
        # print("{} {} {}".format(x, instr[cur][1], y))
        # print(x,y)
        return x == y
    elif is_computed(instr, cur):
        return instr[cur]
    else:
        x = compute(instr, instr[cur][0], humn)
        op = instr[cur][1]
        y = compute(instr, instr[cur][2], humn)
        r = int(eval(str(x) + op + str(y)))
        # print("{} {} {} = {}".format(x, instr[cur][1], y, r))
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
