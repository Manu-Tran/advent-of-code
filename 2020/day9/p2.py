#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os
import time
import sys

def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
preamble = 0
sol = 0
if filename == "input.txt":
    preamble = 25
    sol = 20874512
else :
    preamble = 5
    sol = 127

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    itr = 0
    first = 0
    last = 0
    buff = deque()
    bufsum = 0
    while True:
        if itr == len(arg):
            return None
        m = int(arg[itr])
        # print(bufsum, "(%s %s)" % (first, last))
        if bufsum < sol:
            bufsum += m
            last = m
            buff.append(m)
            itr += 1
        elif bufsum > sol:
            bufsum -= buff.popleft()
            first = buff[0]
        else:
            mini = buff[0]
            maxi = buff[0]
            for n in buff:
                mini = min(n, mini)
                maxi = max(n, maxi)
            return mini+maxi
    return None

res = 127
res = run()
write_file(res)
print(res)
