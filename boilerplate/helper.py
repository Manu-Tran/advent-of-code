#!/usr/bin/env python3

import os
import sys
from itertools import *
from collections import *

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def write_file(solution):
    with open(os.getcwd() + "/last_output", "w") as f:
        f.write(str(solution))

def is_test_case():
    return os.getenv("AOC_INPUT") != "input.txt"

class Node:
    def __init__(self, left, right, parent=None, label=""):
        self.right = right
        self.left = left
        self.label = label
        self.parent = None

    def is_leaf(self):
        return self.right == None and self.left == None

    def is_root(self):
        return parent == None

    def set_parent(self, node):
        self.parent = node

    def set_left(self, node):
        self.left = node
        node.set_parent(self)

    def set_right(self, node):
        self.right = node
        node.set_parent(self)

    def add_left_parent(self, label):
        n = Node(self, None, None, label)
        self.parent = n
        return n

    def add_right_parent(self, label):
        n = Node(None, self, None, label)
        self.parent = n
        return n

def dijkstra(start, grid, get_voisins):
        seen = set()
        dj = defaultdict(lambda:float('inf'))
        dj[start] = 0
        seen.add(start)
        voisin = set()
        voisin.add(start)
        while len(voisin) != 0:
            v = None
            mini = float("inf")
            for c in voisin:
                if v == None:
                    v = c
                    mini = dj[v]
                elif mini > dj[c]:
                    v = c
                    mini = dj[c]
            voisin.remove(v)
            seen.add(v)
            for b in get_voisins(*v, grid):
                if b not in seen:
                    dj[b] = min(dj[v] + 1, dj[b])
                    voisin.add(b)
        return dj
