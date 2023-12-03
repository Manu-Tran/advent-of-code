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
# filename = "test2.txt"

def does_contain_shiny(start_key, data):
    @lru_cache
    def rec(key):
        if (len(data[key]) == 1) and (" no other" in data[key]):
            return 0
        count = 0
        for m in data[key]:
            sp = m.split()
            nb = int(sp[0])
            k = sp[1] + " " + sp[2]
            count += (rec(k) + 1) * nb
        print (key, count)
        return count
    return rec(start_key)

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    data = dict()
    if (arg[-1] == ""):
        arg = arg[:-1]
    for line in arg:
        match = re.findall('(\d* ?\S* \S*) bags?', line)
        data[match[0]] = match[1:]
    return does_contain_shiny("shiny gold", data)

res = run()
write_file(res)
print(res)
