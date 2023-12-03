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

filename = "input.txt"
print("Running ...")

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    maxi = 0
    res = list()
    sums = 0
    for a in arg:
        if a != "":
            sums += int(a)
        else:
            res.append(sums)
            sums = 0
    res.append(sums)
    res.sort()
    return sum(res[-3:])

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)

print("Done !")
