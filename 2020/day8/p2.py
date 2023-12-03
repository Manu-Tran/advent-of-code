#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os
from copy import deepcopy

def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def jump(i, value):
    if value[0] == '+':
        i += int(value[1:])
    else:
        i -= int(value[1:])
    return i

def acc(i, value, acc):
    if value[0] == '+':
        acc += int(value[1:])
    else:
        acc -= int(value[1:])
        i += 1
    return i,acc

def halt(acc, i, prog):
    # print("entering " + str(i))
    new_seen = set()
    while True:
        line = prog[i]
        sp = line.split()
        op = sp[0]
        value = sp[1]
        # print(line)
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
        else :
            return True, -1
        # print(i, acc)
        if i in new_seen :
            return False, acc
        if i == len(prog):
            return True, acc
        new_seen.add(i)


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    acc = 0
    i = 0
    seen = set()
    while True:
        if i in seen :
            return None
        seen.add(i)
        line = arg[i]
        sp = line.split()
        op = sp[0]
        value = sp[1]
        print(line)
        # print(op, value, acc)
        if op == "nop":
            i_bis = i
            if value[0] == '+':
                i_bis += int(value[1:])
            else:
                i_bis -= int(value[1:])
            stop, acc_2 = halt(acc, i_bis, arg)
            if stop:
                return acc_2
            else :
                # print("notstopping")
                i += 1
        elif op == "acc":
            if value[0] == '+':
                acc += int(value[1:])
            else:
                acc -= int(value[1:])
            i += 1
        elif op == "jmp":
            stop, acc_2 = halt(acc, i+1, arg)
            if stop:
                return acc_2
            # else:
                # print("notstopping")
            if value[0] == '+':
                i += int(value[1:])
            else:
                i -= int(value[1:])

res = run()
write_file(res)
print(res)
