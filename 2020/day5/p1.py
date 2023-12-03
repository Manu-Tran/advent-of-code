#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
def run():
    f = open(filename, "r")
    f = f.read()
    f = f.split('\n')
    megamax = 0
    for seq in f:
        maxi = 127
        mini = 0
        mini2 = 0
        maxi2 = 8
        for c in seq:
            if c == "F":
                maxi = (maxi+mini)//2
            elif c == "B":
                mini = (maxi+mini+1)//2
            elif c == "L":
                maxi2 = (maxi2+mini2)//2
            elif c == "R":
                mini2 = (maxi2+mini2+1)//2
            # print(mini,maxi)
            # print(mini2,maxi2)
        megamax = max(megamax, mini * 8 + mini2)
    return megamax

print(run())
