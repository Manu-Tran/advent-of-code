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
preamble = 0
if filename == "input.txt":
    preamble = 25
else :
    preamble = 5

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    itr = 0
    buff = deque()
    while True:
        if itr == len(arg):
            return None
        m = int(arg[itr])
        if itr < preamble :
            buff.append(m)
        else:
            flag = False
            for n in buff:
                if (m-n) in buff:
                    flag = True
                    break
                else:
                    continue
            if not(flag):
                return m
            buff.append(m)
            buff.popleft()
        print(itr)
        itr += 1
    return None

res = 127
res = run()
write_file(res)
print(res)
