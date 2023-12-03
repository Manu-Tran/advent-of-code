#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *

import helper
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
    # argnum = list(map(int, arg))
    start = int(arg[0])
    wait = 0
    buses = list(map(int, filter(lambda x : x != "x", arg[1].split(","))))
    # return start,buses
    while True:
        for bus in buses:
            if start%bus == 0:
                return bus*wait
        wait += 1
        start += 1


if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)
