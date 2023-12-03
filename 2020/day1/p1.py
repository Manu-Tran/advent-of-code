#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *

filename = "input.txt"
def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    return arg

print(run())
