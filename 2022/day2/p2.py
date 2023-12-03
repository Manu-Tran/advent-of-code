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
    rock = 1
    papier = 2
    ciseaux = 3
    win = 6
    lose = 0
    draw = 3
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    scores = list()
    for line in arg:
        score = 0
        l = line.split()
        print(line)
        if l[0] == 'A':
            if l[1] == 'X':
                score += lose
                score += ciseaux
            if l[1] == 'Y':
                score += draw
                score += rock
            if l[1] == 'Z':
                score += win
                score += papier
        if l[0] == 'B':
            if l[1] == 'X':
                score += rock
                score += lose
            if l[1] == 'Y':
                score += draw
                score += papier
            if l[1] == 'Z':
                score += win
                score += ciseaux
        if l[0] == 'C':
            if l[1] == 'X':
                score += lose
                score += papier
            if l[1] == 'Y':
                score += draw
                score += ciseaux
            if l[1] == 'Z':
                score += win
                score += rock
        scores.append(score)

    # argnum = list(map(int, arg))
    return sum(scores)

res = run()
helper.write_file(res)
print(res)

print("Done !")
