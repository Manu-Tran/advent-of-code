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

DIR=["E", "S", "W", "N"]

class Ship:
    def __init__(self, pos, facing):
        self.pos = pos
        self.target = facing

    def direction(self, x, value):
        if "N" == x:
            self.target[1] += value
            pass
        elif "S" == x:
            self.target[1] -= value
            pass
        elif "E" == x:
            self.target[0] += value
            pass
        elif "W" == x:
            self.target[0] -= value
            pass
        elif "L" == x:
            for i in range(value//90):
                self.target[0],self.target[1] = -self.target[1], self.target[0]
            pass
        elif "R" == x:
            for i in range(value//90):
                self.target[0],self.target[1] = self.target[1], -self.target[0]
            pass
        elif "F" == x:
            self.pos[0] += self.target[0]*value
            self.pos[1] += self.target[1]*value
        else:
            pass

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    pos = [0,0]
    target = [10,1]
    a = Ship(pos, target)
    for i in arg:
        a.direction(i[0], int(i[1:]))
        print(a.pos, a.target)
    return abs(a.pos[0]) + abs(a.pos[1])

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)
