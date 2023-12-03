#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def count_w(mat):
    res = ""
    for line in mat:
        for c in line:
            if not(c in res):
                res += c
    return len(res)

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    mat = []
    count = 0
    for line in arg:
        if line == "":
            count += count_w(mat)
            mat = []
        else:
            mat.append(line)
    return count + count_w(mat)


print(run())
