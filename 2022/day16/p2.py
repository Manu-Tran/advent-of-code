#!/usr/bin/python3

from itertools import *
from collections import *
from functools import *
from tqdm import tqdm
import multiprocessing as mp

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

def recursion():
    pass

def new_new_graph(flows, tunnels):
    graph = defaultdict(lambda:defaultdict(lambda:1))
    nodes = set(filter(lambda x: flows[x], tunnels.keys()))
    for i,j,k in product(nodes, nodes, nodes):
        if (i!= j and j!=k and k!=i) and i in tunnels[j] and k in tunnels[j]:
            if (flows[j] == 0 or j == "AA"):
                graph[i][k] = graph[i][j] + graph[j][i]
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

def solve_bis():
    sols = 0
    def dfs(cur_node, graph, flows, seen):
        for


def solve(cur_valve, graph, flows):
    bar = tqdm(total=30*5*100000)
    stck = list()
    seen2 = set()
    @lru_cache(maxsize=None)
    def look_ahead(cur_valves, seen, timers, depth=3):
        max_flow = 0
        index = None
        max_t1 = timers[0]

        index_2 = None
        max_t2= timers[1]
        max_flow_elph = 0
        if depth == 0:
            return 0
        if timers[0] == max(timers):
            if timers[0] <= 0:
                return 0
            max_heur = 0
            cur_valve = cur_valves[0]
            for v in flows:
                if v in seen:
                    continue
                t1 = timers[0]-graph[(cur_valve,v)]-1
                # res = rec(v, seen+(v,), t1) + flows[v]*t1
                res = look_ahead((v, cur_valves[1]), seen+(v,), (t1, timers[1]), depth-1) + flows[v]*t1
                if res >= max_heur:
                    max_heur = res
                    max_flow = flows[v]*t1
                    max_t1 = t1
                    index  = v
        elif timers[1] == max(timers):
            if timers[1] <= 0:
                return 0
            max_heur = 0
            cur_valve = cur_valves[1]
            for v in flows:
                if v in seen or v == index:
                    continue
                t2 = timers[1]-graph[(cur_valve,v)]-1
                # res = rec(v, seen+(v,), t1) + flows[v]*t1
                res = look_ahead((cur_valves[0],v), seen+(index, v,), (max_t1,t2), depth-1) + flows[v]*t2
                if res >= max_heur:
                    max_heur = res
                    max_flow_elph = flows[v]*t2
                    max_t2 = t2
                    index_2  = v
        return max_flow + max_flow_elph

    @lru_cache(maxsize=None)
    def rec(cur_valves, seen, timers):
        # bar.update(1)
        # print(seen)
        if timers[1] == 0:
            return 0
        if timers[0] == 0:
            return 0
        print(seen)
        print(timers)
        index = None
        max_t1= timers[0]
        max_flow = 0
        depth = 1
        if timers[0] == max(timers):
            max_heur = 0
            cur_valve = cur_valves[0]
            for v in flows:
                if v in seen:
                    continue
                t1 = timers[0]-graph[(cur_valve,v)]-1
                # res = rec(v, seen+(v,), t1) + flows[v]*t1
                res = look_ahead((v, cur_valves[1]), seen+(v,), (t1, timers[1]), depth) + flows[v]*t1
                print(v,res)
                if res >= max_heur:
                    max_heur = res
                    max_flow = flows[v]*t1
                    max_t1 = t1
                    index  = v
            print("choosing", index, max_t1)
        index_2 = None
        max_t2= timers[1]
        max_flow_elph = 0
        if timers[1] == max(timers):
            max_heur = 0
            cur_valve = cur_valves[1]
            for v in flows:
                if v in seen or v == index:
                    continue
                t2 = timers[1]-graph[(cur_valve,v)]-1
                # res = rec(v, seen+(v,), t1) + flows[v]*t1
                res = look_ahead((cur_valves[0],v), seen+(index, v,), (max_t1,t2), depth) + flows[v]*t2
                print(v,res)
                if res >= max_heur:
                    max_heur = res
                    max_flow_elph = flows[v]*t2
                    max_t2 = t2
                    index_2  = v
            print("choosing elph", index_2, max_t2)
        if index:
            if index_2:
                seen = seen + (index, index_2)
            else:
                seen = seen + (index,)
                index_2 = cur_valves[1]
        else:
            index = cur_valves[0]
            if index_2:
                seen = seen + (index_2,)
            else:
                index_2 = cur_valves[1]

        if index:
            if index_2:
                seen2.add((index, 26-max_t1, "you"))
                seen2.add((index_2, 26-max_t2, "elph"))
            else:
                seen2.add((index, 26-max_t1, "you"))
                index_2 = cur_valves[1]
        else:
            index = cur_valves[0]
            if index_2:
                seen2.add((index_2, 26-max_t2,"elph"))
            else:
                index_2 = cur_valves[1]

        print(seen2)
        if len(flows.keys())+1 <= len(seen):
            return max_flow + max_flow_elph

        return rec((index, index_2), seen, (max_t1,max_t2)) + max_flow + max_flow_elph
    res = rec(("AA","AA"), ("AA",), (26, 26))
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
