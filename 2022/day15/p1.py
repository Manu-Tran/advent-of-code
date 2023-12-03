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
    Y = 2000000
else:
    Y = 10
dry_run = not(os.getenv("RUN_MODE", "DRY_RUN") == "SUBMIT")

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)

print("Running with \"dry_run:{}\" ...".format(dry_run))
def man_dist(a,b):
    return(abs(a[0] - b[0]) + abs(a[1] - b[1]))

def run():
    f = open(filename, "r")
    f = f.read()
    arg = f.split('\n')
    if (arg[-1] == ""):
        arg = arg[:-1]
    beacons = dict()
    sensors = set()
    beacons_set = set()
    for line in arg:
        if line != "":
            print(line)
            r = re.match("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
            sensor = (int(r.group(1)), int(r.group(2)))
            beacon = (int(r.group(3)), int(r.group(4)))
            beacons_set.add(beacon)
            # beacons[(beacon)].append(sensor)
            sensors.add(sensor)
            beacons[sensor] = beacon
    in_range = list()
    for sensor in sensors:
        # if(sensor != (20,14)):
        #     continue
        m = man_dist(sensor,beacons[sensor])
        print("yolo")
        if (sensor[1] < Y and Y < (sensor[1]+m)):
            y_dist = Y - (sensor[1])
            wide = (m*2+1) - y_dist*2
            n = (sensor[0]-wide//2)
            in_range.append((n, n + wide-1))

        elif (sensor[1] > Y and Y > (sensor[1]-m)):
            y_dist = abs(Y - (sensor[1]))
            wide = (m*2+1) - y_dist*2
            print(m)
            print(wide)
            n = sensor[0]-wide//2
            in_range.append((n, n + wide-1))
    count = 0
    in_range.sort()
    print(in_range)
    last_interv = (None,None)
    in_the_way = set()
    for b in beacons_set :
        if b[1] == Y:
            in_the_way.add(b[1])
    print("yy ", in_the_way)
    no_intersec = list()
    for i in in_range:
        if len(no_intersec) == 0:
            no_intersec.append(i)
        else:
            while True:
                if len(no_intersec) == 0:
                    no_intersec.append(i)
                    break
                j = no_intersec.pop()
                if i[1] >= j[0]:
                    i = min(i[0], j[0]), max(j[1], i[1])
                else:
                    no_intersec.append(j)
                    no_intersec.append(i)
                    break
    for interv in no_intersec:
        if last_interv == (None,None):
            last_interv = interv
            print(interv)
            count += interv[1] - interv[0]
            print("from {} to {}".format(interv[0], interv[1]))
            print(count)
        else:
            print(interv)
            print(last_interv)
            # if (interv[0] > last_interv[0]) and (last_interv[1] > interv[1]):
            #     print("skipping")
            #     continue
            if (interv[0] <= last_interv[1]):
                count += max(interv[1], last_interv[1])-last_interv[1]-1
                for b in in_the_way:
                    print(b)
                    if b >= last_interv[1]-1 and b <= max(interv[1], last_interv[1]):
                        count -= 1
                print("from {} to {}".format(max(interv[1], last_interv[1]), last_interv[1]-1))
            else:
                count += max(interv[1], last_interv[1])-interv[0]
                for b in in_the_way:
                    print(b)
                    if b >= interv[0] and b <= max(interv[1], last_interv[1]):
                        count -= 1
                print("from {} to {}".format(max(interv[1], last_interv[1]), interv[0]))
            print(count)
    return count

if not(dry_run):
    helper.blockPrint()
else:
    helper.enablePrint()
res = run()
helper.write_file(res)
helper.enablePrint()
print(res)

print("Done !")
