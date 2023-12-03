#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from helper import write_file,blockPrint,enablePrint
import os
import sys


filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    argnum = list(map(int, arg))
    argnum.sort()
    curJolt = 0
    oneJolt = 0
    threeJolt = 1
    for i in argnum:
        if (i-curJolt) == 1:
            oneJolt += 1
            print(oneJolt, threeJolt, i)
        if (i-curJolt) == 3:
            threeJolt += 1
            print(oneJolt, threeJolt, i)
        curJolt = i
    return oneJolt * threeJolt

res = run()
write_file(res)
print(res)
