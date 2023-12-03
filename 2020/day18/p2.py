#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

import re
import helper
import os
import sys
#71
filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

class lolteger:
    def __init__(self, n):
        self.value = n

    def __add__(self, other):
        return lolteger(self.value + other.value)

    def __sub__(self, other):
        return lolteger(self.value * other.value)

    def __mul__(self, other):
        return lolteger(self.value + other.value)

    def __str__(self):
        return(str(self.value))


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    sums = 0
    for line in arg:
        print(line)
        # line = (line.replace("*", "time").replace("+", "*").replace("time", "+"))
        line = (line.replace("*", "-").replace("+","*"))
        print(line)
        p = re.compile("(\d+)")
        line =p.sub("lolteger(\\1)", line)
        print(line)
        # print(lolteger(10)+lolteger(2) - lolteger(3))
        sums += (eval(line)).value
    return sums

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
