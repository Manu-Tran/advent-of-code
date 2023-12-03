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
if filename == "input.txt":
    X = 0
    Y = 4000000
else:
    X = 0
    Y = 20
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))
def man_dist(a,b):
    return(abs(a[0] - b[0]) + abs(a[1] - b[1]))

def find_int(y, sensors, beacons):
    in_range = list()
    for sensor in sensors:
        # if(sensor != (20,14)):
        #     continue
        m = man_dist(sensor,beacons[sensor])
        if (sensor[1] < y and y < (sensor[1]+m)):
            y_dist = y - (sensor[1])
            wide = (m*2+1) - y_dist*2
            n = (sensor[0]-wide//2)
            # print(sensor, beacons[sensor], (n, n+wide-1))
            in_range.append((n, n + wide-1))

        elif (sensor[1] >= y and y >= (sensor[1]-m)):
            y_dist = abs(y - (sensor[1]))
            wide = (m*2+1) - y_dist*2
            n = sensor[0]-wide//2
            # print(sensor, beacons[sensor], (n, n+wide-1))
            in_range.append((n, n + wide-1))

    in_range.sort()
    no_intersec = deque()
    # print("ranges",in_range)
    for i in in_range:
        if len(no_intersec) == 0:
            no_intersec.append(i)
        else:
            k = i
            while True:
                # if y == 11:
                    # print(no_intersec)
                    # print(k)
                if len(no_intersec) == 0:
                    no_intersec.append(k)
                    break
                j = no_intersec.pop()
                # print(j)
                # if y == 11:
                #     print(k[1], j[0])
                if k[0] <= j[1]:
                    k = min(k[0], j[0]), max(j[1], k[1])
                else:
                    no_intersec.append(j)
                    no_intersec.append(k)
                    break
    return no_intersec

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    beacons = dict()
    sensors = set()
    for line in arg:
        if line != "":
            print(line)
            r = re.match("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
            sensor = (int(r.group(1)), int(r.group(2)))
            beacon = (int(r.group(3)), int(r.group(4)))
            # beacons[(beacon)].append(sensor)
            sensors.add(sensor)
            beacons[sensor] = beacon
    for y in tqdm(range(0,Y)):
        # print("y", y)
        res = find_int(y,sensors,beacons)
        # print(res)
        if len(res) >= 2:
            if res[0][1]+1 <= Y:
                y,x= (y, res[0][1]+1)
                # print(x,y)
                return(x*4000000 + y)
        print()



helper.blockPrint()
# else:
#     helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
