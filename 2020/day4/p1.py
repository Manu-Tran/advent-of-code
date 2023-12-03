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

def is_valid(passport):
    print(passport)
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for f in fields:
        if f in passport.keys():
            continue
        return False
    return True

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    count = 0
    passport = dict()
    for line in arg:
        if line == "":
            if is_valid(passport):
                count += 1
            passport = dict()
        tmp = line.split()
        for field in tmp :
            a = field.split(":")
            passport[a[0]] = a[1]
    # argnum = list(map(int, arg))
    return count

if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()
print(res)
