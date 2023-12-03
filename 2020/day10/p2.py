#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os
import sys

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def get_count(k, liste):
    @lru_cache
    def rec(i):
        if i == (len(liste)-1):
            return 1
        somme = 0
        i_max = i
        while (liste[i_max] <= (liste[i] + 3)):
            if i_max == (len(liste)-1):
                i_max += 1
                break
            i_max += 1
        for j in range(i+1,i_max):
            somme += rec(j)
        return somme
    return rec(k)

sol = 8
sol = 19208

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    argnum = [0] + list(map(int, arg))
    argnum.sort()
    argnum.append(argnum[-1]+3)
    # a = get_count(8, argnum)
    print([get_count(i, argnum) for i in range(0,len(argnum))])
    return get_count(0, argnum)

# blockPrint()
res = run()
write_file(res)
# enablePrint()
print(res)
