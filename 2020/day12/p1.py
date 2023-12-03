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
        self.face = facing

    def direction(self, x, value):
        if "N" == x:
            self.pos[1] += value
            pass
        elif "S" == x:
            self.pos[1] -= value
            pass
        elif "E" == x:
            self.pos[0] += value
            pass
        elif "W" == x:
            self.pos[0] -= value
            pass
        elif "L" == x:
            self.face = DIR[DIR.index(self.face)-(value//90)]
            pass
        elif "R" == x:
            self.face = DIR[(DIR.index(self.face)+(value//90))%4]
            pass
        elif "F" == x:
            return self.direction(self.face, value)
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
    face = "E"
    a = Ship(pos, face)
    for i in arg:
        a.direction(i[0], int(i[1:]))
        print(a.pos, a.face)
    return abs(a.pos[0]) + abs(a.pos[1])

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)
