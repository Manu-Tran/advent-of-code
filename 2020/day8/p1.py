#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os
import sys

def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    acc = 0
    i = 0
    seen = set()
    while i < len(arg):
        line = arg[i]
        sp = line.split()
        op = sp[0]
        value = sp[1]
        # print(op, value, acc)
        # if acc > 100:
        #     return
        if op == "nop":
            i += 1
        elif op == "acc":
            if value[0] == '+':
                acc += int(value[1:])
            else:
                acc -= int(value[1:])
            i += 1
        elif op == "jmp":
            if value[0] == '+':
                i += int(value[1:])
            else:
                i -= int(value[1:])
        if i in seen :
            return acc
        seen.add(i)

res = run()
write_file(res)
print(res)
