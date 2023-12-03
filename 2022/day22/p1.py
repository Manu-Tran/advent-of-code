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
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

RIGHT=0
DOWN=1
LEFT=2
UP=3

print("Running with \"dry_run:{}\" ...".format(dry_run))

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    old_cmd = arg[-1]
    arg = arg[:-2]
    maze = list()
    max_len = 0
    for line in arg:
        for i,c in enumerate(line):
            if c != " ":
                offset = i
                break
        maze.append((offset, line.replace(" ", "")))
    cmd = []
    b = ""
    for c in old_cmd:
        if c in "1234567809":
            b += c
        else:
            cmd.append((int(b), c))
            b = ""
    cmd.append((int(b), "H"))
    cur_pos = (0,0)
    facing = RIGHT
    # cur_pos = forward(4, cur_pos, RIGHT, maze)
    # cur_pos = forward(6, cur_pos, DOWN, maze)
    # cur_pos = forward(4, cur_pos, LEFT, maze)
    # cur_pos = forward(4, cur_pos, LEFT, maze)
    # cur_pos = forward(2, cur_pos, DOWN, maze)
    # cur_pos = forward(10, cur_pos, RIGHT, maze)
    # cur_pos = forward(10, cur_pos, LEFT, maze)
    # cur_pos = forward(10, cur_pos, RIGHT, maze)
    # cur_pos = forward(10, cur_pos, LEFT, maze)
    # cmd = []
    # print(cmd)
    for c in cmd:
        cur_pos = forward(c[0], cur_pos, facing, maze)
        if c[1] == "R":
            facing = (facing + 1)%4
        elif c[1] == "L":
            facing = (facing - 1 + 4)%4
    print(cur_pos, facing)
    return 1000*(cur_pos[0]+1) + 4*(cur_pos[1]+1+maze[cur_pos[0]][0]) + facing

# def update_pos(old_c, new_c, maze):
#     i = 0
#     # print(old_c, new_c)
#     if old_c[1] != new_c[1]:
#         new_c = (new_c[0], new_c[1]%len(maze[new_c[0]][1]))
#     else:
#         new_c = (new_c[0]%len(maze), new_c[1])
#     new_y = new_c[0]
#     x = (new_c[1] + maze[old_c[0]][0] - maze[new_c[0]][0])
#     while x < 0 or x >= len(maze[new_y][1]):
#         if old_c[0] < new_c[0] or (old_c[0] == len(maze)-1):
#             i += 1
#         else:
#             i -= 1
#         # print(i)
#         new_y = (new_c[0]+i)%len(maze)
#         x = (new_c[1] + maze[old_c[0]][0] - maze[new_y][0])
#     if x >= len(maze[new_y][1]):
#         x = x%len(maze[new_y][1])
#     return (new_y,x)

def update_pos_vert(old_c, new_c, maze):
    is_down = old_c[0] < new_c[0]
    new_c = new_c[0]%len(maze), new_c[1]
    #Setup new offset
    x = (new_c[1] + maze[old_c[0]][0] - maze[new_c[0]][0])
    i = 0
    new_y = new_c[0]
    while x < 0 or x >= len(maze[new_y][1]):
        print(x,new_y)
        print(len(maze[new_c[0]][1]))
        if is_down:
            i += 1
        else:
            i -= 1
        new_y = (i + new_c[0])%len(maze)
        x = (new_c[1] + maze[old_c[0]][0] - maze[new_y][0])
    return (new_y, x)

def update_pos_hor(old_c, new_c, maze):
    is_right = old_c[1] < new_c[1]
    new_c = new_c[0],new_c[1]%len(maze[new_c[0]][1])
    return new_c

def get_maze(c, maze):
    return maze[c[0]][1][c[1]]


def forward(n, pos, face, maze):
    print("moving",n,face,pos)
    for _ in range(n):
        # print(pos)
        if face == RIGHT:
            next = (pos[0], pos[1]+1)
            next_upd = update_pos_hor(pos, next, maze)
        elif face == DOWN:
            next = (pos[0]+1, pos[1])
            next_upd = update_pos_vert(pos, next, maze)
        elif face == LEFT:
            next = (pos[0], pos[1]-1)
            next_upd = update_pos_hor(pos, next, maze)
        elif face == UP:
            next = (pos[0]-1, pos[1])
            next_upd = update_pos_vert(pos, next, maze)
        print("looking", next_upd)
        c = get_maze(next_upd,maze)
        print("getting", c)
        if c == ".":
            pos = next_upd
        else:
            return pos
    return pos



if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
