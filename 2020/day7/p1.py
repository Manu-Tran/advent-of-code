#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
import os
import sys
import re

def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

def does_contain_shiny(start_key, data):
    @lru_cache
    def rec(key):
        if "shiny gold" in data[key]:
            return True
        else :
            if (len(data[key]) == 1) and ("no other" in data[key]):
                return False
            res = False
            for m in data[key]:
                if rec(m):
                    return True
        return False
    return rec(start_key)


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    data = dict()
    if (arg[-1] == ""):
        arg = arg[:-1]
    for line in arg:
        match = re.findall('(\S* \S*) bags?', line)
        data[match[0]] = match[1:]
    count = 0
    for key in data.keys():
        if does_contain_shiny(key, data):
            count += 1
    return count

res = run()
write_file(res)
print(res)
