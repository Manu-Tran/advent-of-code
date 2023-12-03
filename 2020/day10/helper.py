#!/usr/bin/env python3

import os
import sys

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))
