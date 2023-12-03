#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm

import re
import helper
import os
import sys

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"

print("Running ...")

def get_rule(index, indexes):
    @lru_cache(maxsize=None, typed=False)
    def rec(index):
        helper.enablePrint()
        if index == 8:
            cur_res = rec(int(42))
            res = set()
            print(cur_res)
            for s in cur_res:
                res.update(set(map(lambda x: s+x, cur_res)))
            res.update(cur_res)
            return res
        elif index == 11:
            cur_res = rec(int(42))
            cur_res_2 = rec(int(31))
            res = set()
            print(cur_res)
            for s in cur_res:
                res.update(set(map(lambda x: s+x, cur_res_2)))
            return res
            return
        res = set()
        med_res = set()
        for c in indexes[index].split():
            if c.isnumeric():
                cur_res = rec(int(c))
                # print("rec call", index, c,cur_res)
                if len(med_res) == 0:
                    med_res = cur_res
                else:
                    new_med_res = set()
                    for s in med_res:
                        new_med_res.update(set(map(lambda x: s+x, cur_res)))
                    # if (len(new_med_res) == 0):
                        # print(index, c)
                        # return
                    med_res = new_med_res
                continue
            elif c == "|":
                res.update(med_res)
                med_res = set()
                continue
            reg = re.match("\"(.*)\"", c)
            if reg:
                res.add(reg.group(1))
        res.update(med_res)
        # print(index, res)
        if(len(res) == 0):
            return False
        return res
    return rec(index)


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    flag = False
    count = 0
    indexes = dict()
    for line in arg:
        if len(line) == 0:
            # print(indexes)
            res = get_rule(0,indexes)
            flag = True
            # print("final rule",  res)
            continue
        if flag:
            if line in res:
                count += 1
            continue
        indexes[int(line[:line.find(":")])] = line[line.find(":")+2:]
    return count

# if filename == "input.txt":
#     helper.blockPrint()
res = run()
helper.write_file(res)
# if filename == "input.txt":
#     helper.enablePrint()
print(res)

print("Done !")
