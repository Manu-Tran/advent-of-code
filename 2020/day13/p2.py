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

print("Running ...")

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    # argnum = list(map(int, arg))
    buses = list(map(int, map(lambda x : 1 if "x" == x else x , arg[1].split(","))))
    n = reduce(lambda acc,x : acc*x,  buses, 1)
    x = 0
    print(n)
    for i,k in enumerate(buses):
        print("i =", i)
        if k == 1 :
            continue
        n_bis = n//k
        print(n_bis,"k =",k)
        v = 1
        while ((v*n_bis)%k != 1):
            # print(v, (v*n_bis)%k)
            v += 1
            if (v*n_bis)%k == 0:
                return x
        print("check", v*n_bis % k)
        x += v * n_bis * (k-i)
        print(n,x%n)
    return x%n

#1068788




helper.enablePrint()
if filename == "input.txt":
    helper.blockPrint()
res = run()
helper.write_file(res)
if filename == "input.txt":
    helper.enablePrint()

print(res)
print("Done !")
