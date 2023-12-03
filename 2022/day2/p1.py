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

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    rock = 1
    papier = 2
    ciseaux = 3
    win = 6
    lose = 0
    draw = 3
    if (arg[-1] == ""):
        arg = arg[:-1]
    scores = list()
    for line in arg:
        score = 0
        l = line.split()
        print(line)
        if l[0] == 'A':
            if l[1] == 'X':
                score += rock
                score += draw
            if l[1] == 'Y':
                score += papier
                score += win
            if l[1] == 'Z':
                score += ciseaux
                score += lose
        if l[0] == 'B':
            if l[1] == 'X':
                score += rock
                score += lose
            if l[1] == 'Y':
                score += papier
                score += draw
            if l[1] == 'Z':
                score += ciseaux
                score += win
        if l[0] == 'C':
            if l[1] == 'X':
                score += rock
                score += win
            if l[1] == 'Y':
                score += papier
                score += lose
            if l[1] == 'Z':
                score += ciseaux
                score += draw
        scores.append(score)

    # print(scores)
    print(sum(scores))
    # argnum = list(map(int, arg))
    return sum(scores)

res = run()
helper.write_file(res)
print(res)

print("Done !")
