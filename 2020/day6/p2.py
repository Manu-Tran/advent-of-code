#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os

def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def is_in_all(c, mat):
    for line in mat:
        if c in line:
            continue
        else :
            return False
    return True

def count_w(mat):
    res = ""
    for c in mat[0]:
        if is_in_all(c, mat):
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


res = run()
write_file(res)
print(res)
