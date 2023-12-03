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
from copy import copy

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))
ORE = 0
CLAY = 1
OBS = 2
GEO = 3
RES = [ORE,CLAY,OBS,GEO]

def check_supply(project, supply):
    for i in range(len(project)):
        if project[i] > supply[i]:
            return False
    return True

def update_state(robots, supply):
    return(supply[0] + robots[0], supply[1] + robots[1], supply[2] + robots[2], supply[3] + robots[3])

def build(project, resource,robots,supply):
    return(tuple(robots[r] if r != resource else robots[r] +1 for r in RES),(supply[0] - project[0], supply[1] - project[1], supply[2] - project[2], supply[3]))


def simulate(robots, state, blueprint):
    @lru_cache(maxsize=None)
    def rec(robots, state, timer, id):
        # bar.update(1)
        if timer == 1:
            state = update_state(robots, state)
            return robots, state, str(33-timer) + "pass-"
        max_r, max_s = robots, state
        flag = False
        # Prioritise GEO
        cur_c = ""
        max_c = ""
        new_state = update_state(robots, state)
        if check_supply(blueprint[GEO],state):
            r, s = build(blueprint[GEO], GEO, robots, new_state)
            rp, sp, c = rec(r, s, timer-1, id)
            if sp[3] > max_s[3]:
                max_r, max_s, max_c = rp, sp, c
                cur_c = "geo-"
        elif check_supply(blueprint[OBS],state):
            r, s = build(blueprint[OBS], OBS, robots, new_state)
            rp, sp, c = rec(r, s, timer-1, id)
            if sp[3] > max_s[3]:
                max_r, max_s, max_c = rp, sp, c
                cur_c = "obs-"

        else:
            can_build = [check_supply(blueprint[project], state) if project != "id" else None for project in blueprint]
            flag = all(can_build[:-1])
            maxi = [int((max([blueprint[b][i] for b in RES])*timer-state[i]) / timer) for i in [ORE, CLAY, OBS]]
            too_many_robots = [robots[i] > maxi[i] for i in [ORE, CLAY, OBS]]
            # print(state, maxi, too_many_robots)
            # print(too_many_robots)
            for project in blueprint:
                if project in ["id", 2,3]:
                    continue
                if too_many_robots[project]:
                    continue
                if project == CLAY and too_many_robots[OBS]:
                    continue
                if can_build[project]:
                    r, s = build(blueprint[project], project, robots, new_state)
                    rp, sp, c = rec(r, s, timer-1, id)
                    if sp[3] > max_s[3]:
                        max_r, max_s, max_c = rp, sp, c
                        cur_c = "ore-" if project==0 else "clay-" if project==1 else "ylo---"
        if not(flag) and max(new_state) < 20:
        # if not(flag):
            r, s, c = rec(robots, new_state, timer-1, id)
            if s[3] > max_s[3]:
                max_r, max_s, max_c = r, s, c
                cur_c = "pass-"
        # print(max_s, timer)
        return max_r, max_s, max_c + str(33-timer) + cur_c
    print(blueprint["id"])
    return rec(robots, state, 32, blueprint["id"])

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    blpts = list()
    for line in arg:
        match = re.match("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", line)
        blueprint = dict()
        blueprint[ORE] = (int(match.group(2)), 0, 0)
        blueprint[CLAY] = (int(match.group(3)), 0, 0)
        blueprint[OBS] = (int(match.group(4)), int(match.group(5)), 0)
        blueprint[GEO] = (int(match.group(6)), 0, int(match.group(7)))
        blueprint["id"] = (int(match.group(1)))
        blpts.append(blueprint)
    scores = list()
    for b in tqdm(reversed(blpts)):
        print(b)
        scores.append((*simulate((1,0,0,0), (0,0,0,0), b), b["id"]))
        print(scores)
    res = []
    for score in scores:
        res.append((score[1][-1]))
    res.sort()
    print(res)
    if len(res) >= 3:
        return res[-3]* res[-2] * res[-1]
    else:
        return res[-2] * res[-1]



if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
