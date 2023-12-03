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

def is_field_valid(key,field):
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
    if key == "byr":
        return len(field) == 4 and int(field) <= 2002 and int(field) >= 1920
    elif key == "iyr":
        return len(field) == 4 and int(field) <= 2020 and int(field) >= 2010
    elif key == "eyr":
        return len(field) == 4 and int(field) >= 2020 and int(field) <= 2030
    elif key == "hgt":
        if field[-2:] == "cm":
            size = int(field[:-2])
            return size >= 150 and size <= 193
        elif field[-2:] == "in":
            size = int(field[:-2])
            return size >= 59 and size <= 76
        else :
            return False
    elif key == "hcl":
        return len(field) == 7 and field[0] == "#" and all([c in "1234567890abcdef" for c in field[1:]])
    elif key == "ecl":
        return field in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return len(field) == 9 and all([c in "1234567890" for c in field[1:]])
    else:
        return True

def is_valid(passport):
    print(passport)
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for f in fields:
        if f in passport.keys():
            print(f, passport[f], is_field_valid(f, passport[f]))
        if f in passport.keys() and is_field_valid(f, passport[f]):
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
