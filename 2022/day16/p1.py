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
import copy

filename = os.getenv("AOC_INPUT")
if not(filename):
    filename = "input.txt"
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))

def get_dist(c, graph):
    dist = dict()
    to_look = deque()
    to_look.append((c,0))
    while len(to_look) != 0:
        n,i = to_look.popleft()
        dist[n] = i
        for v in graph[n]:
            if v not in dist:
                to_look.append((v,i+1))
    return dist

def new_graph(flows, tunnels):
    graph = dict()
    summits = flows.keys()
    for s in summits:
        d = get_dist(s, tunnels)
        for sp in summits:
            if s != sp:
                graph[(s,sp)] = d[sp]
            graph[("AA",s)] = d["AA"]
    return graph


def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    tunnels = defaultdict(lambda:[])
    flows = dict()
    for line in arg:
        print(line)
        r = re.match("Valve (..) has flow rate=(\d*); tunnels? leads? to valves? (.*)", line)
        valve = r.group(1)
        flow = r.group(2)
        tunnel = r.group(3).split(", ")
        tunnels[valve] = tunnel
        if int(flow) != 0:
            flows[valve] = int(flow)
        # print(valve,flow,tunnels)
    # print(get_dist("AA", tunnels))
    # return solve_bis("AA", ("AA",), new_graph(flows, tunnels), flows)
    return solve("AA", new_graph(flows, tunnels), flows)

def solve_bis(cur_valve, seen, graph, flows):
    @lru_cache
    def rec(cur_valve, seen, timer):
        if len(seen) == len(flows):
            return 0
        pot_gain = defaultdict(lambda:0)
        max_flow = 0
        max_heur = 0
        max_v = cur_valve
        for v in flows:
            if v in seen:
                continue
            for vp in flows:
                if v == vp or vp in seen:
                    continue
                for vpp in flows:
                    if v == vpp or vp == vpp or vpp in seen:
                        continue
                    for vppp in flows:
                        if v == vppp or vp == vppp or vpp == vppp or vppp in seen:
                            continue
                        t1 = timer-graph[(cur_valve,v)]-1
                        t2 = t1-graph[(v,vp)]-1
                        t3 = t2-graph[(vp,vpp)]-1
                        t4 = t3-graph[(vpp,vppp)]-1
                        pot_gain[v] = max(t1 * flows[v] + t2 * flows[vp] + t3 * flows[vpp] + t4* flows[vppp], pot_gain[v])
                        if pot_gain[v] > max_heur:
                            max_v = v
                            max_heur = pot_gain[v]
                            max_flow = t1 * flows[v]
                            max_t1= t1
            print(v)
        if max_v == cur_valve:
            return 0
        print("opening", max_v, max_t1, pot_gain)
        return max_flow + rec(max_v, seen+(max_v,), timer-graph[(cur_valve, max_v)]-1)
    return rec(cur_valve, seen, 30)




def solve(cur_valve, graph, flows):
    bar = tqdm(total=30*5*100000)
    stck = list()
    @lru_cache(maxsize=None)
    def look_ahead(cur_valve, seen, timer, depth=0):
        max_flow = 0
        index = cur_valve
        if depth == 5:
            return 0
        for v in flows:
            if v in seen:
                continue
            t1 = timer-graph[(cur_valve,v)]-1
            res = look_ahead(v, seen+(v,), t1, depth+1) + flows[v]*t1
            if res >= max_flow:
                max_flow = res
                index  = v
        return max_flow

    @lru_cache(maxsize=None)
    def rec(cur_valve, seen, timer):
        # bar.update(1)
        # print(seen)
        if timer == 0:
            return 0
        max_flow = 0
        max_heur = 0
        index = None
        max_t1= 0
        for v in flows:
            if v in seen:
                continue
            t1 = timer-graph[(cur_valve,v)]-1
            # res = rec(v, seen+(v,), t1) + flows[v]*t1
            res = look_ahead(v, seen+(v,), t1) + flows[v]*t1
            print(v,res)
            if res >= max_heur:
                max_heur = res
                max_flow = flows[v]*t1
                max_t1 = t1
                index  = v
        print("choosing", index, max_t1)
        return rec(index, seen + (index,), max_t1) + max_flow
    res = rec(cur_valve, ("AA",), 30)
    # print(stck)
    return res


if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
